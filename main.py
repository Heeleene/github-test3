from Covid_pack.Jeu import Data
from Covid_pack.estimateurs import Estimateurs
from Covid_pack.Etendue import Etendue
from Covid_pack.moyenne import Moyenne
from Covid_pack.Variance import Variance
from Covid_pack.Mode import Mode






d1=Data.charger_jeu_donnees('donnees hospitalieres par classe et age')
print(d1)

md1=Mode(d1,['rea'])
md1.calcul_mode_2()










