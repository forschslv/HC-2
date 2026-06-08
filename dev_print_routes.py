import importlib
app = importlib.import_module('app').app
print('Registered endpoints:')
for rule in sorted(app.url_map.iter_rules(), key=lambda r: r.rule):
    methods = ','.join(sorted(rule.methods - {'HEAD','OPTIONS'}))
    print(f"{rule.endpoint:30} -> {rule.rule:30}  methods=[{methods}]")

