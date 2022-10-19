#arquivo pra chamar todos os arquivos em sequencia e evitar erro do flask de referência circular

import app
from models import Torcedor
import views

#criar tudo no banco, caso não tenha sido criado
app.db.create_all()
#rodar aplicação
app.app.run(debug=True)

