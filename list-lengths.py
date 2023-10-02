# copy two or three of the lists you made from the previous exercises, or make up two or three new lists
# print out a series of statements that tells us how long each list is

# make two or three new lists
regions = ['mondstadt', 'liyue', 'sumeru', 'fontaine']
archons = ['venti', 'nahida', 'furina']
elements = ['anemo', 'geo', 'dendro', 'hydro', 'pyro']

# retrieve the len of list regions
region_count = len(regions)
archon_count = len(archons)
element_count = len(elements)

print('\nthe regions for this prompt are:')
for region in regions:
	print(region.title())

print(f'\nthe length of the list regions = {region_count}')

print('\nthe archons for this prompt are:')
for archon in archons:
	print(archon.title())

print(f'\nthe length of the list archons = {archon_count}')

print('\nthe elements for this prompt are:')
for element in elements:
	print(element.title())

print(f'\nthe length of the list elements = {element_count}')

