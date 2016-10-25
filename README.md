# accesslog-audit
一个网站的apache开启了access日志，每小时生成一个w日志文件，以当前日期时间为后缀。例如：special.XXXXXX.com.cn.2016101001
需要分析日志，判断是否存在web攻击。

脚本第一部分是根据命令行输入的参数，获取用户指定的日志文件夹。遍历每个日志文件，合并到一个新的文件。

第二部分是定义了常见web攻击的特征字符串，如select/union/java，常见structs攻击特征字符串，如java/ognl，常见的webshell操作字符串，如eval/excute
使用正则f逐行分析日志文件，命中的内容复制到结果文件中
