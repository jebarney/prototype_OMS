import sqlite3


# Query the database
with sqlite3.connect("store.db") as db:
    cur = db.cursor()

# # Drop table
# cur.execute("DROP TABLE precios")

# # Create new table
# cur.execute("""CREATE TABLE precios (
# 		vendedor TEXT,
# 		fecha_pedido TEXT,
# 		num_cliente INT,
# 		cliente TEXT,
# 		oc_ventas TEXT,
# 		cajas INT,
# 		marca TEXT,
# 		pedido_lertek TEXT,
# 		no_pedido INT
# 	)""")

# Input data in table
muchos_pedidos = [
					('COSTEÑA', '9/1/2021', '1009674', 'OPERADORA DE REYNOSA, S A DE C V', '16612-20', '47', 'COSTE', '', '441824'),
					('Carlos Medina', '9/1/2021', '1394', 'CENTROS COMERCIALES MARTINEZ DE NUEVO LAREDO, S.A. DE C.V.', 'CMS-001', '74', 'COSTE', 'A1202', '441839'),
					('Gerardo Rodriguez', '9/1/2021', '1046', 'FEDERICO EDUARDO ALVARADO LECHUGA', 'GR09005', '747', 'COSTE', 'A1217', '450249')
				]
cur.executemany("INSERT INTO precios VALUES (?,?,?,?,?,?,?,?,?)", muchos_pedidos)

db.commit()