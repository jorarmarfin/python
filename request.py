import requests

host='http://practical.test'
url=host+'/wp-json/hubconnector/v1/dspace_asset'
data={
    "dspace_asset_title": "Ante el cambio climático Soluciones Prácticas",
    "dspace_asset_status": "publish",
    "dspace_asset_abstract": "Presentamos nuestras áreas de trabajo en desarrollo bajo en carbono, adaptación al cambio climático y reducción del riesgo de desastres. Además, compartimos nuestras competencias temáticas ante el Cambio Climático: energía limpia, gestión sostenible de bosques, agricultura sostenible, reducción de riesgo de desastres y resiliencia, y gestión integrada de recursos hídricos y suelo.",
    "dspace_asset_uri": "http://hdl.handle.net/11283/622041",
    "dspace_asset_authors": [
        {"tag": "Lewis"},
        {"tag": "Mark"}
    ],
    "dspace_asset_issue_date": "21/03/2017",
    "dspace_asset_oai_identifier": "https://infohub.practicalaction.org/handle/11283/622042",
    "dspace_asset_publisher": "Practical Action, Latin America",
    "dspace_asset_downloads": [
        {
            "name": "1671398201932521295.pdf",
            "image": "https://infohub.practicalaction.org/bitstream/handle/11283/622041/1671398201932521295.pdf.jpg",
            "size": "4.157Mb",
            "mimetype": "PDF",
            "description": "",
            "download": "https://infohub.practicalaction.org/bitstream/handle/11283/622041/1671398201932521295.pdf"
        }
    ],
    "dspace_asset_rights": [
        {"tag": "Practical Action"}
    ],
    "dspace_asset_externallinks": [
        {"tag": "https://solucionespracticas.org.pe/Agroforesteria-sostenible-Recuperando-los-bosques-amazonicos"}
    ],
    "dspace_asset_urls": [],
    "dspace_asset_collections": [
        {"tag": "Cambio climático"},
        {"tag": "Agricultura sostenible"},
        {"tag": "reducción del riesgo"},
        {"tag": "Energía limpia"}
    ],
    "dspace_asset_subjects": [
        {"tag": "Agriculture"},
        {"tag": "Climate Change"},
        {"tag": "Disasters"}
    ],
    "dspace_asset_format": [
        {"tag": "Publicity Materials"}
    ],
    "dspace_asset_language": [
        {"tag": "es"}
    ]
}
result = requests.post(url,json=data)

print(result)