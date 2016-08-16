#!/usr/bin/python
""">> cassoap << command line query tool by Tamas Budavari <budavari@pha.jhu.edu>
Usage: cassoap.py [options] sqlfile(s)

Options:
        -s url    : URL of XML Web Service (default: pha)
        -q query  : specify query on the command line
        -o file   : set output file name (default: stdout)
        -h	  : show this message"""

import sys, os, getopt, string, httplib, xml.sax
from xml.sax.handler import ContentHandler
from xml.sax.saxutils import escape
            
class CasService:
    soap = """<?xml version="1.0" encoding="utf-8"?>\r
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"\r
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\r
      <soap:Body>\r
        <GetStream xmlns="http://skyservice.pha.jhu.edu">\r
          <sqlcmd>%s</sqlcmd>\r
        </GetStream>\r
      </soap:Body>\r
    </soap:Envelope>\r
    """
    soapaction = "http://skyservice.pha.jhu.edu/GetStream"
    headers = {"Content-Type":"text/xml; charset=utf-8",
               "SOAPAction": soapaction}
    def __init__(self,host='skyservice.pha.jhu.edu',
                 path='/devel/CasService/CasService.asmx',
                 port=httplib.HTTP_PORT):
        self.host, self.path, self.port = host, path, port
        self.debuglevel = 0
    def GetStream(self,sqlcmd):
        body = self.soap % escape(sqlcmd)
        blen = len(body)
        requestor = httplib.HTTP(self.host, self.port)
        requestor.putrequest('POST', self.path)
        requestor.putheader('Host', self.host)
        requestor.putheader('Content-Type', 'text/xml; charset="utf-8"')
        requestor.putheader('Content-Length', str(blen))
        requestor.putheader('SOAPAction', self.soapaction)
        requestor.endheaders()
        requestor.send(body)
        (status_code, message, reply_headers) = requestor.getreply()
        if self.debuglevel > 0:
            print "** Status code:", status_code
            print "** Status message:", message
            print "** Headers:\n", reply_headers
        return requestor.getfile()

class CasStreamHandler(ContentHandler):
    """Crude extractor for CAS (stream) results
       print contents of <anyType> and newline at </CasItem>"""
    def __init__(self,ofp=None,gettype=0):
        try: self.write = ofp.write
        except: self.write = sys.stdout.write
        self.gettype = gettype
    def startDocument(self):
        self.in_item, self.item = 0, ''
    def startElement(self, name, attrs):
        if name == 'anyType':
            self.in_item, self.item = 1, ''
            if self.gettype: self.type = attrs.getValue('xsi:type')
        elif name == 'faultstring':
            self.exception = 1
            self.in_item, self.item = 1, ''
    def characters(self, ch):
        if self.in_item: self.item = self.item + ch
    def endElement(self, name):
        if name == 'anyType':
            self.write(self.item+' '); self.in_item = 0
            if self.gettype: self.write('('+self.type+') ')
        elif name == 'CasItem': self.write(os.linesep)
        elif name == 'faultstring':
            self.write('*** ERROR: ' + \
                       string.replace(self.item,'-->', os.linesep+'-->') + \
                       os.linesep)

def usage(status, msg=''):
    print __doc__
    if msg: print '-- ERROR: %s' % msg
    sys.exit(status)
    
def main(argv):
    "Parse command line and do it..."
    queries, outfile = [], sys.stdout
    try: optlist, args = getopt.getopt(argv[1:],'s:q:o:h?')
    except getopt.error, e: usage(1,e)
    # options
    for o,a in optlist:
        if   o=='-s': url = a
        elif o=='-q': queries.append(a)
        elif o=='-o': outfile = open(a,'w')
        else: usage(0)
    # Enqueue queries in files
    for fname in args:
        try: queries.append(open(fname).read())
        except IOError, e: usage(1,e)
    # Run all queries
    cas = CasService()
    parser = xml.sax.make_parser()
    parser.setContentHandler(CasStreamHandler(outfile))
    for qry in queries:
        res = cas.GetStream(qry)
        parser.parse(res)
    outfile.close()

# - - - - - - - - - - - - 
if __name__=='__main__':
    main(sys.argv)
# - - - - - - - - - - - - 




