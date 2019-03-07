# tronado
利用tronado框架设计网页 这个框架在前端模板可以执行所有的python代码 例如引用包:
{% import requests %}
{% set resp = requests.get() %} # 使用set关键词来设置变量


这个框架跟flask\django框架前端继承模板方式不同: 
flask\django: 
{% block content %} {% endblock %}
tronado
{% block content %} {% end %}
