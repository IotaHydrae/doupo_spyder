from get_url import get_url
def html_outputer(name_list):
    c=1
    fout = open('folder/开始阅读.html', 'w')
    fout.write("<html>")

    fout.write("<body>")
    fout.write("<br />")
    fout.write("<table border=\"0px\">")
    for name in name_list:
        fout.write("<tr>")
        fout.write('<a href="{0}.txt">{1}</a><br>'.format(c, name))
        fout.write("<tr>")
        c+=1
    fout.write("</table>")
    fout.write("<br />")
    fout.write("</body>")

    fout.write("</html>")

if __name__ == '__main__':
    root_url = 'https://doupocangqiong1.com/1/list_piaotian/'
    zhangjie_url, zhangjie_name = get_url(root_url)
    html_outputer(zhangjie_name)