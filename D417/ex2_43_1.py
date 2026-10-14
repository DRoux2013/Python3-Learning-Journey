bread = ['bagels', 'baguette', 'ciabatta', 'crumpet']
try:
    crumpet_index = bread.index('crumpet')
except:
    crumpet_index = 'No crumpet bread found'
print(crumpet_index)