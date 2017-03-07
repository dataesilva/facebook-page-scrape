import csv

#Welcome Message
print('FB text search')

#Search paramters
polls = ['poll ', 'polling', 'polls', 'poll.']
deplorable = ['deplorable', 'deplorables']
benghazi = ['benghazi']
twitter = ['twitter', 'tweet']
rigged = ['rigged', 'rigging', 'rig', 'rigs']
pence = ['pence', 'mike pence']
kaine = ['kaine', 'time kaine']
gun = ['gun', 'guns', 'gun control', '2nd ammendment', '2 ammendment', 'background check',
       'background checks', '2ndamendment', 'gun ownership']
terrorism = ['terrorist', 'terrorists', 'isis', 'isil', 'al qaeda', 'daesh', 'terror attack',
             'terror attacks']
fpolicy = ['un ', 'nato']
trade = ['free trade', 'tpp', 'nafta', 'foreign trade', 'tariff', 'trade tax', 'import', 'export',
         'imports', 'exports']
careact = ['obamacare', 'aca', 'affordable care act', 'healthcare coverage']
entitlements = ['medacaid', 'medicare', 'social security']
opioid = ['opiod', 'meth', 'heroin', 'overdose']

#Begin search 1, general form
with open('FB Data text only.csv', 'r') as oldfile, open('test.csv', 'w') as newfile:
    lower_f = (row.lower() for row in oldfile)
    csv_f = csv.reader(lower_f, delimiter = ',')
    csvwrite = csv.writer(newfile)
    for row in csv_f:
        if any(polls in row[2] for polls in polls):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	#Still in progress from here on
  if any(deplorable in row[2] for deplorable in deplorable):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(benghazi in row[2] for benghazi in benghazi):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(twitter in row[2] for twitter in twitter):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(rigged in row[2] for rigged in rigged):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(pence in row[2] for pence in pence):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(kaine in row[2] for kaine in kaine):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(gun in row[2] for gun in gun):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(terrorism in row[2] for terrorism in terrorism):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(fpolicy in row[2] for fpolicy in fpolicy):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(trade in row[2] for trade in trade):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(careact in row[2] for careact in careact):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(entitlements in row[2] for entitlements in entitlements):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])

	if any(opioid in row[2] for opioid in opioid):
            csvwrite.writerow(row+[1]) #Still an issue with writing file correctly
        else: csvwrite.writerow(row+[0])


#Signal all done
print('Done')
