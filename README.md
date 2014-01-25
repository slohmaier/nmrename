nmrename
========

Noneus' Mass Renaming Tool

help
====
Help&nbsp;for&nbsp;nmrename&nbsp;0.1<br />
<br />
USAGE:<br />
nmrename.py:&nbsp;[FILES&nbsp;...]&nbsp;[COMMAND&nbsp;...]&nbsp;...<br />
<br />
Positions&nbsp;are&nbsp;indexes&nbsp;for&nbsp;the&nbsp;filename.&nbsp;Start&nbsp;an<br />
index&nbsp;with&nbsp;"-",&nbsp;if&nbsp;you&nbsp;want&nbsp;to&nbsp;start&nbsp;index&nbsp;counting<br />
from&nbsp;the&nbsp;end&nbsp;of&nbsp;the&nbsp;filename.<br />
<br />
COMMANDS:<br />
-h&nbsp;--help&nbsp;:&nbsp;Print&nbsp;this&nbsp;help&nbsp;output.<br />
-d&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Rename&nbsp;folderstructure&nbsp;too.&nbsp;Be&nbsp;careful&nbsp;with&nbsp;"/"'s!<br />
-f&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Don't&nbsp;ask.&nbsp;Just&nbsp;rename.<br />
-cu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Convert&nbsp;filename&nbsp;to&nbsp;upper&nbsp;case.<br />
-cl&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Convert&nbsp;filename&nbsp;to&nbsp;lower&nbsp;case.<br />
-cc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Convert&nbsp;filename&nbsp;to&nbsp;camel&nbsp;case.<br />
-sd&nbsp;#1&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Remove&nbsp;string&nbsp;#1&nbsp;from&nbsp;all&nbsp;filenames.<br />
-sr&nbsp;#1&nbsp;#2&nbsp;:&nbsp;Replace&nbsp;string&nbsp;#1&nbsp;with&nbsp;string&nbsp;#2.<br />
-si&nbsp;#1&nbsp;#2&nbsp;:&nbsp;Insert&nbsp;string&nbsp;#2&nbsp;at&nbsp;position&nbsp;#1.<br />
-fn&nbsp;#1&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;Insert&nbsp;filecount&nbsp;line&nbsp;from&nbsp;#1.<br />
-fi&nbsp;#1&nbsp;#2&nbsp;:&nbsp;Insert&nbsp;filecount&nbsp;line&nbsp;from&nbsp;#2&nbsp;at&nbsp;position&nbsp;#1.<br />
-exif&nbsp;#1&nbsp;&nbsp;:&nbsp;Rename&nbsp;from&nbsp;EXIF-Data&nbsp;with&nbsp;a&nbsp;pattern.&nbsp;(e.g.&nbsp;%Y.%M.%D_%h:%m:%s_%O%e)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pattern&nbsp;Elements:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%Y:&nbsp;year&nbsp;(e.g.&nbsp;2012)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%M:&nbsp;month&nbsp;(e.g.&nbsp;06)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%D:&nbsp;day&nbsp;(e.g.&nbsp;09)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%h:&nbsp;hour&nbsp;(e.g.&nbsp;14)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%m:&nbsp;minute&nbsp;(e.g.&nbsp;40)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s:&nbsp;second&nbsp;(e.g.&nbsp;09)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%o:&nbsp;complete&nbsp;original&nbsp;filename<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%e:&nbsp;extension&nbsp;(e.g.&nbsp;.jpg)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%O:&nbsp;filename&nbsp;without&nbsp;extension<br />
-tag&nbsp;#1&nbsp;&nbsp;&nbsp;:&nbsp;Rename&nbsp;from&nbsp;audio&nbsp;tags&nbsp;with&nbsp;a&nbsp;pattern.&nbsp;(e.g.&nbsp;"%a&nbsp;-&nbsp;%A&nbsp;-&nbsp;%t&nbsp;-&nbsp;%y%e")<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pattern&nbsp;Elements:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%a:&nbsp;artist<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%A:&nbsp;album<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%AA:&nbsp;albumartist<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%t:&nbsp;title<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%y:&nbsp;year<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%tn:&nbsp;track-number<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%Tn:&nbsp;total-tracks<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%e:&nbsp;file&nbsp;extension<br />
