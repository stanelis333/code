Uzduotis:

Susiskirstykite į komandas po du.
Pasirinkite duomenų rinkinį iš Kaggle (bent 10 000 eilučių). Stulpelių bent 10
Pritaikykite mažiausiai du prižiūrimo mokymosi (supervised learning) modelius pasirinktam duomenų rinkiniui.
Parašykite išvadas apie savo atradimus, pasirinkimus ir rezultatus. Pateikite bent tris logiškas išvadas.
Rezultatus ir išvadas galite pateikti lentelėje arba Word dokumente.
Užduočiai skirtas laikas: visa rytojaus diena. Atsiskaitymas po 8 valandų nuo užduoties pradžios.
Svarbu: ChatGPT naudojimas yra griežtai draudžiamas. Jei bus pastebėta, kad darbas atliktas naudojant ChatGPT, gausite 0 balų.


About data
This dataset is collected from National Health Insurance Service in Korea. All personal information and sensitive data were excluded.
The purpose of this dataset is to:

Analysis of body signal
Classification of drinker or not

#Colunm Description
#Sex    male, female
#age    round up to 5 years
#height round up to 5 cm[cm]
#weight [kg]    
#sight_left eyesight(left)     
# sight_right   eyesight(right)
# hear_left hearing left, 1(normal), 2(abnormal)    
# hear_right    hearing right, 1(normal), 2(abnormal)  
# SBP   Systolic blood pressure[mmHg]  - Tai yra didžiausias spaudimas kraujagyslėse. Aukštas sistolinis kraujospūdis gali reikšti hipertenziją, 
širdies ligas ir padidėjusią insulto riziką.
# DBP   Diastolic blood pressure[mmHg]  - Tai yra mažiausias spaudimas kraujagyslėse. Aukštas diastolinis kraujospūdis taip pat gali reikšti hipertenziją 
ir kitas širdies bei kraujagyslių ligas.
# BLDS  BLDS or FSG(fasting blood glucose)[mg/dL]  - Gliukozės kiekis kraujyje matuojamas po 8–12 valandų nevalgymo. Aukštas gliukozės kiekis gali rodyti 
diabetą arba gliukozės tolerancijos sutrikimą.
# tot_chole total cholesterol[mg/dL]  - Bendras cholesterolis. Aukštas bendro cholesterolio kiekis gali reikšti padidėjusią širdies ir kraujagyslių ligų riziką.  
# HDL_chole HDL cholesterol[mg/dL]  - „gerasis“ cholesterolis. Didesnis DTL cholesterolio kiekis yra susijęs su mažesne širdies ligų rizika, 
nes jis padeda pašalinti cholesterolį iš arterijų.
# LDL_chole LDL cholesterol[mg/dL]  - „bloguoju“ cholesteroliu. Aukštas MTL cholesterolio kiekis gali sukelti aterosklerozę ir padidinti širdies ligų riziką.
# triglyceride  triglyceride[mg/dL] -riebalų tipas, randamas kraujyje. Aukštas trigliceridų kiekis gali padidinti širdies ligų ir insulto riziką.
# hemoglobin    hemoglobin[g/dL]    -  Žemas hemoglobino kiekis gali rodyti anemiją, o aukštas – galimus sveikatos sutrikimus, pvz., dehidrataciją ar plaučių ligas.
# urine_protein protein in urine, 1(-), 2(+/-), 3(+1), 4(+2), 5(+3), 6(+4)  - Aukštas baltymų kiekis šlapime gali rodyti inkstų pažeidimą ar ligą.

# serum_creatinine  serum(blood) creatinine[mg/dL]  - Kreatininas yra atliekų produktas, susidarantis raumenų veiklos metu, ir išsiskiria per inkstus. Aukštas serumo kreatinino lygis gali rodyti inkstų funkcijos sutrikimą.

# SGOT_AST  SGOT(Glutamate-oxaloacetate transaminase) AST(Aspartate transaminase)[IU/L] -AST yra fermentas, randamas kepenyse ir širdies raumenyse. Aukštas AST lygis gali rodyti kepenų ar širdies pažeidimą.

# SGOT_ALT  ALT(Alanine transaminase)[IU/L] - ALT yra fermentas, kuris daugiausiai randamas kepenyse.  Aukštas ALT lygis gali rodyti kepenų pažeidimą ar ligą.

# gamma_GTP y-glutamyl transpeptidase[IU/L] - GGT yra fermentas, kuris dalyvauja aminorūgščių ir peptidų metabolizme. Aukštas GGT lygis gali rodyti kepenų ligas, tulžies latakų pažeidimą ar piktnaudžiavimą alkoholiu.
# SMK_stat_type_cd  Smoking state, 1(never), 2(used to smoke but quit), 3(still smoke)  
# DRK_YN    Drinker or Not
