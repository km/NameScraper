from flask import Flask, redirect, url_for, request
import json
import requests
import namemc
app = Flask(__name__)
# /droptime body: {"name":"yourusername"}
@app.route('/droptime',methods = ['POST'])
def droptime():
   if request.method == 'POST':
      name = str(request.json.get('name'))
      print(name)
      return str(int(namemc.namemc.getDroptime(name)))
# /list?length=&lang=&searches=&length_op=      
@app.route('/list',methods = ['GET'])
def nlist():
   if request.method == 'GET':
      length = str(request.args.get('length'))
      lang = str(request.args.get('lang'))
      searches = str(request.args.get('searches'))
      length_op = str(request.args.get('length_op'))
      nmc = namemc.namemc(length, length_op, lang, searches)
      li = nmc.getList()
      flist = ""
      for x in li:
         flist += x+"\n"
      flist = flist.strip()   
      return flist

if __name__ == '__main__':
      app.run(port=80)
                            
