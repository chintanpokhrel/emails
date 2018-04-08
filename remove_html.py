def removeHtmlAndOtherCrap(filename):
	htmlAndOtherCrap = set(['p', 'td', 'padding', 'table', 'width', 'P', 'font', 'tr', 'height', '10px', 'style', 'style', 'size', 'border', '100', 'text', 'color', 'li', 'margin', 'http', 'com', 'left', 'right', 'align', 'href', 'center', 'div', '0px', 'br', 'title', 'html', '_blank', 'www', 'important', 'family', 'adjust', 'tbody', 'line', 'yrs', 'target', 'class', 'none', 'top', 'amp', 'img', 'cellspacing', 'gmail', 'serif', 'sansHelvetica', '0pt', 'ref', 'https', 'span', 'nbsp', '1px', 'cellpadding', 'webkit', 'Arial', 'valign', 'background', 'display', 'Helvetica', 'src', 'enf', 'solid', 'sans', 'alt', 'decoration', 'weight', 'mso', 'block', '3D', 'bottom', 'email', '10', '0000000000', 'bgcolor', 'auto', '12', '12px', 'rspace', 'max', '5px', '20px', 'strong', '15', 'lspace', 'ffffff', 'org', 'png', 'jpg', 'id', 'collapse', '65535', 'normal', 'spacer', 'null', 'gif', 'images', 'ms', 'vertical', 'bold', '20', 'float', 'click', 'media', 'QE', 'content', 'Sans', 'Margin', 'eml', 'min', 'body', 'td', 'TD', 'view', 'type', 'css', 'DTD', 'dtd', 'xhtml1', 'xhtml', 'image' ])

	fout = open(filename + ".nohtml", 'w')
	with open(filename) as fin:
		for word in fin:
			if len(word)>2 and word[-3:-1] != 'px' and word[0:-1] not in htmlAndOtherCrap:
				fout.write(word)
	fout.close() 
	

import sys
removeHtmlAndOtherCrap(sys.argv[1])	
