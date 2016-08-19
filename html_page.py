#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

class HtmlReturn:
	def htmlstring(self, imagens, content, x, web):
		report = content
		imagens = imagens.replace(str(os.getcwd()), "").replace("/", "")



#		begin = '<td><img style="max-width:80px" src="static/galaxies/'
		begin = '<td><img style="max-width:80px" src="/'

		middle = '">'
		end = "</td>"


		imagens = imagens.split("<br>")
		content = content.split("<br>")

		for i in range(0, x):
			imagens[i] = begin + imagens[i] + middle + content[i] + end

		imagens = str(imagens)

		imagens = imagens.replace(",", "<br>")
		redo = ["'", "[", "]", "\n"]
		for index in redo:
			imagens = imagens.replace(index, "")



		print imagens

		htmlpage = '''
	<script>var $prehashval = "";
				function loop()
				{
					if (location.hash.slice(1)!=$prehashval)
						hashChanged();

					$prehashval = location.hash.slice(1);
					setTimeout("loop()", 100);
				}
				function hashChanged()
				{
					var $output;
					switch (location.hash.slice(1))
					{
						case "page1":
							document.getElementById('page1').style.display = "";
							document.getElementById('page2').style.display = "none";
							break;
						case "page2":
							document.getElementById('page1').style.display = "none";
							document.getElementById('page2').style.display = "";
							break;
						default:
							$output = location.hash.slice(1);
					}
				}
				loop();</script>

		<div style="" id="page1">
					 <title> [File Uploaded!] </title>
					 <a href="javascript:history.back();location.reload();">Go Back</a>
																 <h1>
								 GALAXIES:
								 </h1>
								 <h2><a href="#page2">see the report</a></h2>
									 <p>
									 ''' + web + imagens + '''


												 </p>
					</div>

					<div style="display:none" id="page2">
					<a href="javascript:history.back()">Go Back</a>

					<h2><a href="#page1">see the galaxies</a></h2>
					 ''' + report + '''

					</div>


		'''


		return htmlpage
