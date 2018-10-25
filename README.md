# 上手教程
## 环境配置
1. Python版本为2.7，采用3.0版本请自行修改源码中编码相关代码。
2. 安装python虚拟环境`virtualenv venv`。
3. 切换至虚拟环境`source venv/bin/activate`。
4. 安装依赖`pip install -r requirements.txt`。
5. 安装jena和fuseki（尽量下载3.7之前的版本，否则会出现配置文件不兼容的情况，也可以自行修改配置文件）。OS X系统可用brew安装，如下所示。
    ```bash
    brew install jena fueseki
    ```

## 准备数据
有两种方法。
1. 事先将三元组数据导入tdb
    ```bash
    tdbloader --loc tdb kg_demo_movie.nt
    ```

2. 略过此步。等服务器启动后在[管理后台](localhost:3030)上传数据。

## 运行服务器
```bash
fuseki-server --config fuseki_conf.ttl
```

## 问题集锦
1. 启动服务器时报以下错误
    ```code
    #model_inf was aborted because of NodeTableThrift/Write
    ```
    #### 推测原因
    InfModel里baseModel和content属性两者不兼容。
    ```code
    <#model_inf> a ja:InfModel ;
        ja:baseModel <#tdbGraph> ;
        # ja:content
    ```
   #### 解决
   注释掉其中的一项。例如，将content注释掉，等服务器启动后，再上传本体文件。

# 目录结构
## Data文件夹
包含ER图模型文件和创建数据库、表，插入所有数据的sql文件。用户可以直接使用sql文件导入数据到mysql中。

## kg\_demo_movie文件夹
- crawler中的movie_crawler用于从The Movie DB下载数据，用户需要自己去网站注册账号，申请API KEY。在脚本中填入自己的API KEY，填写mysql相关参数即可运行。用户需要额外下载的包:requests和pymysql。tradition2simple用于将繁体字转为简体字（声明一下，我找不到该文件的出处了，我是从网上找到的解决方案，如果有用户知道该作者，麻烦告知，我会备注）。
- KB_query文件夹包含的是完成整个问答demo流程所需要的脚本。
	-  "external_dict"包含的是人名和电影名两个外部词典。csv文件是从mysql-workbench导出的，按照jieba外部词典的格式，我们将csv转为对应的txt。
	-  "word_tagging"，定义Word类的结构（即我们在REfO中使用的对象）；定义"Tagger"类来初始化词典，并实现自然语言到Word对象的方法。
	-  "jena\_sparql_endpoint"，用于完成与Fuseki的交互。
	-  "question2sparql"，将自然语言转为对应的SPARQL查询。
	-  "question_temp"，定义SPARQL模板和匹配规则。
	-  "query\_main"，main函数。在运行"query_main"之前，读者需要启动Fuseki服务。

## ontology.owl
通过protege构建的本体，用户可以直接用protege打开，查看或修改。

## kg\_demo\_movie_mapping.ttl
根据d2rq mapping language编辑的映射文件，将数据库中的数据映射到我们构建的本体上。

## kg\_demo_movie.nt
利用d2rq，根据mapping文件，由Mysql数据库转换得到的RDF数据。

## fuseki_conf.ttl
fuseki server配置文件，指定推理引擎，本体文件路径，规则文件路径，TDB路径等

## rules.ttl
规则文件，用于基于规则的推理。
