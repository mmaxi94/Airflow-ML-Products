import json, requests, csv, os

def get_products(producto):
    limit=5 #primeras 5 publicaciones

    url = 'https://api.mercadolibre.com/sites/MLA/search?q=%s&limit=%s#json' % (producto, limit)
    response = requests.get(url)
    response.raise_for_status()
    respuesta =json.loads(response.text)

    datos=[]

    header = ['id','titulo','precio','moneda','condicion','envio_gratis','link']
    datos.append(header)
    for i in range(0, len(respuesta['results'])):

        linea = [i+1, respuesta['results'][i]['id'],respuesta['results'][i]['title'],respuesta['results'][i]['price'],
                 respuesta['results'][i]['currency_id'],respuesta['results'][i]['condition'],respuesta['results'][i]['shipping']['free_shipping'],
                 respuesta['results'][i]['permalink']]
        datos.append(linea)

    nombre_archivo="/opt/airflow/plugins/Productos.txt"

    with open(nombre_archivo, 'w', newline='') as csvfile:
        outputWriter = csv.writer(csvfile, delimiter='|')
        outputWriter.writerows(datos)
