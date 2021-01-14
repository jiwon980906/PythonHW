import copy
x = {'python': {'version': '2.7'}, 'script': {'name': 'hello.py'}}
a = x
b = x.copy()
c = copy.deepcopy(x)
x['python']['version'] = '3.6'
print(a['python']['version'], b['python']['version'], c['python']['version'])
