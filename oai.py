from sickle import Sickle

sickle = Sickle('https://infohub.practicalaction.org/oai/request')
records = sickle.ListRecords(metadataPrefix='oai_dc')
print(records.next())
#https://infohub.practicalaction.org/oai?metadataPrefix=oai_dc&verb=ListRecords
#https://infohub.practicalaction.org/oai/request?verb=ListRecords&metadataPrefix=oai_dc