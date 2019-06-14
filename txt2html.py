import sys
import os

def txt2html(txt_file, html_file):
     idx = 0
     with open(txt_file) as f:
         while True:
             line = f.readline()
             line = lines.decode("utf-8").encode("gbk")

             if not lines:
                 break
             # print(lines)
             try:
                 line_write = '<table><tr><td>' + str(idx) + ' url: ' + line.split('\t')[0] + ' reason: ' + \
                              line.split('\t')[1] + ' judge: ' + line.split('\t')[2] + '</td></tr></table>' + '\n' + \
                              '<td><img src="' + line.split('\t')[0] + '" width=216 border=1 /></td></tr></table><br/><br/>'
                 with open(html_file, 'a') as file:
                     file.write(line_write + '\n')
                 idx += 1
             except Exception as e:
                 print('line parse errors')
                 print(e)
                 continue

 if __name__ == "__main__":
     if len(sys.argv) < 2:
         print('please input txt file')
     else:
         txt_file = sys.argv[1]
         html_file = os.path.basename(txt_file).split('.')[0] + '.html'
         if os.path.exists(html_file):
             os.remove(html_file)
         txt2html(txt_file, html_file)
