import app
from models import Torcedor
import views

app.db.create_all()
app.app.run(debug=True)