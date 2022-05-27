在allure生成结果文件temp中，添加executor.json，就添加了报告中运行器信息，一般运行器会自动生成
同样目录下添加environment.xml和environment.properties两个文件，生成环境信息
同样目录下添加categories.json文件，生成对应的类别信息，默认通过正则表达式对应以下值
Default ["failed", "broken", "passed", "skipped", "unknown"]

以上文件需要在生成静态文件前创建到报告结果文件夹中，之后执行生成静态文件的命令才会把相应数据添加
如果需要显示趋势内容，需要在生成静态报告前，把history文件copy到报告结果文件夹中，才会显示历史趋势

@allure.epic("设置后，类中的多个函数在报告中看作一个用例")

locust基于接口测试进行client实例，向目标系统发出HTTP请求，可以返回详细的表数据，用户行为越精确，越能精准的测试负载能力