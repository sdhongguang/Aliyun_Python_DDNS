
1、运行文件为：ddns.py

2、将ddns.py 和 filecontrol.py放在同一目录下

3、程序运行时会在 所在目录创建 ipAddres 文件 用来存放 更新后的IP地址

4、运行逻辑：
    get_ip()获取 本地的公网IP地址，获得的地址与 ipAddress文件中的IP地址比对。
    如果没有文件则创建文件，并使用获取到的公网IP写入 ipAddress 。
    如果IP地址比对后，发现不同，使用 get_record()来获取DNS解析信息。
    使用获取到的公网IP，比对 DNS解析信息。
    如果不同，则使用change_record(ip) 来更新IP地址
    ///之所以加入文件对比，是防止程序频繁的使用aliyun的API，造成IP被封。///

5、ak = 'XXX'    sc = 'XXX'  SubDomain = 'XXX.Domain.com'
    ak: AccessKeyID     sc:AccessKeySecret      SubDomain:二级域名
    此三项参数从Aliyun账户中获得。
    特别注意：：
        AccessKey 如果使用 子用户AccessKey，一定要注意权限管理。
            需要的权限是： AliyunDNSFullAccess
            我一直以为是AliyunDomainFullAccess，结果折腾死我了。
        此程序只支持二级域名的解析，并且此二级域名必须已经存在，此程序不会创建域名。

6、系统需要安装的插件：
    
    sudo apt install Python3 #系统自带可忽略。
    sudo apt install Python3-pip
    sudo apt install curl
    sudo pip3 install Aliyun-Python-SDK-Core
    
7、建立定时任务
    我现在是更改的 /etc/crontab 文件，增加了一行：
    
    */10 *  * * *   root    /usr/bin/python3.6 /home/yourname/getrecord.py
    # 意思是 每10分钟执行一次。但我并不知道这么做是不是有用。太新手了。。。

8、郁闷不，不小心把 accessKey传上去了，真坑。
    请自己新建一个文件，account.py
    
    ak = 'your_AccessKeyId'
    sc = 'your_AccessKeySecret'
    SubDomain = 'your_SubDomain'