# AprilCalib log 20
# CalibRig::mode=2d
# @ Fri Dec  3 18:20:59 2021

from numpy import array
U=array([[56.46430969238281, 233.5926818847656, 117.667366027832, 176.7291870117188, 110.2833709716797, 287.9286193847656, 231.3603515625, 172.0797119140625, 45.67359161376953],
       [383.3632507324219, 390.9686279296875, 386.0045471191406, 388.6125183105469, 444.9847106933594, 448.8876953125, 447.7440490722656, 446.5007934570312, 443.6738586425781]], dtype='float64');
Xw=array([[699.5044555664062, 1299.504516601562, 899.5044555664062, 1099.504516601562, 899.5044555664062, 1499.504516601562, 1299.504516601562, 1099.504516601562, 699.5044555664062],
       [99.50446319580078, 99.50446319580078, 99.50446319580078, 99.50446319580078, 299.5044555664062, 299.5044555664062, 299.5044555664062, 299.5044555664062, 299.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[639.9547972745495, 0, 330.4851848544751],
       [0, 638.9110435887836, 245.1703815508487],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.05063754889992699,
       0.01412734850779954,
       0.00601399574501483,
       0.0003990056730786835,
       0], dtype='float64');
CovK=array([[0.1312415709040957, 0.1250034998503291, 0.0595761935274146, -0.07282440352336197, 0.0001110816328846029, 0.0005117754851517194, -3.197368333397776e-05, 2.114363755382088e-05, -0.001128822236627205],
       [0.1250034998503385, 0.1293589795437728, 0.05728968756296712, -0.0689435453007879, 0.0001512402885041599, 0.0003760391146013201, -3.874123831730726e-05, 1.915134214815818e-05, -0.0009139414730139703],
       [0.05957619355259256, 0.0572896875877103, 0.492305023991855, -0.06674322471199177, 4.969626758755882e-05, 0.00104597171088904, -3.367486491036475e-05, 0.0002004248327539085, -0.002566047127788895],
       [-0.07282440350941763, -0.06894354528715949, -0.06674322459854028, 0.3855210948102652, -0.0002782056520503759, 0.0001852638368296984, 0.0001628239358614604, -3.060412987830525e-05, 0.0001041050987910419],
       [0.0001110816328728461, 0.0001512402884931485, 4.969626748120788e-05, -0.0002782056520522214, 7.701698426014373e-06, -4.172989265695253e-05, -3.07893405181346e-07, 3.23982938910972e-08, 7.649952583903857e-05],
       [0.0005117754852339885, 0.0003760391146784377, 0.001045971711092688, 0.0001852638365627546, -4.172989265670564e-05, 0.0002728263292893987, 8.244592537281228e-07, 4.053610912722972e-07, -0.0005323180430448682],
       [-3.197368332831143e-05, -3.874123831177341e-05, -3.367486486211955e-05, 0.0001628239358624345, -3.078934051826106e-07, 8.24459253851035e-07, 9.340188735375422e-08, -1.558089999382292e-08, -1.292212306785524e-06],
       [2.114363756384563e-05, 1.915134215801082e-05, 0.0002004248327525968, -3.060412992434606e-05, 3.239829393374035e-08, 4.053610911901596e-07, -1.558090001338296e-08, 9.065204399068257e-08, -1.003792929396962e-06],
       [-0.001128822236795643, -0.0009139414731719421, -0.002566047128032964, 0.0001041050994145764, 7.649952583845697e-05, -0.0005323180430443158, -1.292212306502163e-06, -1.00379292949523e-06, 0.001078332907967959]], dtype='float64');
# rms=0.194345
r0=array([-0.3823428363870627,
       -0.02280467438469307,
       0.04888079955481318], dtype='float64');
t0=array([205.5385808090894,
       -51.37224863191444,
       3241.712609939344], dtype='float64');
Covr0=array([[1.121473947940432e-06, 2.704598526947285e-08, -1.549586741443992e-07],
       [2.704598554421545e-08, 1.940246019807857e-06, 1.205970931750186e-07],
       [-1.549586741182496e-07, 1.20597093223866e-07, 4.597168107596151e-08]], dtype='float64');
Covt0=array([[12.73977695009265, -1.436821237594552, -1.344358926022008],
       [-1.43682123469087, 9.735034051901593, 2.381090275220906],
       [-1.344358925187722, 2.381090275547728, 3.61669392627021]], dtype='float64');
r1=array([-0.3715026039903305,
       0.1256810407254272,
       -0.09118162891379247], dtype='float64');
t1=array([-821.1209098206139,
       45.8884466564872,
       4360.991476317091], dtype='float64');
Covr1=array([[1.183563127966554e-06, 1.266488522772361e-07, 5.118155013775366e-08],
       [1.26648852510994e-07, 1.326915323980896e-06, 1.578013392043477e-07],
       [5.118155017106449e-08, 1.578013391891192e-07, 3.534399947971275e-08]], dtype='float64');
Covt1=array([[22.65586360144107, -2.882919952246112, 1.521734841780758],
       [-2.882919946981441, 17.99795588812734, 3.509505751369049],
       [1.521734843161791, 3.509505751016869, 5.770060136424831]], dtype='float64');
r2=array([-0.02838843697021458,
       -0.01776001234047625,
       -0.1357029316439701], dtype='float64');
t2=array([-1104.119103050438,
       -42.32188270623916,
       3469.206624989331], dtype='float64');
Covr2=array([[1.304025432367282e-06, 1.474369065087676e-08, 4.108117052450653e-08],
       [1.474369082129508e-08, 1.284446556151317e-06, -4.830572479197513e-08],
       [4.10811705198837e-08, -4.830572479865393e-08, 8.626020095645149e-09]], dtype='float64');
Covt2=array([[14.53066266634471, -1.87353952977481, 2.029920444642571],
       [-1.873539526369455, 11.74618568937092, 2.352371838471477],
       [2.029920445592291, 2.352371837975419, 5.36538452965541]], dtype='float64');
r3=array([-0.2284771445142097,
       -1.143093312455889,
       0.1188383606127907], dtype='float64');
t3=array([-673.2241895313056,
       -374.8951506153327,
       458.3026274130559], dtype='float64');
Covr3=array([[7.99342647411252e-07, 1.545639522041009e-07, -3.64954751733561e-07],
       [1.545639524276576e-07, 1.07243322589345e-06, 2.502259695468454e-08],
       [-3.649547517105789e-07, 2.502259707419664e-08, 2.194941503944164e-07]], dtype='float64');
Covt3=array([[0.3862936152227053, -0.06930156889301425, 0.1065064245352868],
       [-0.06930156880910049, 0.3122400200985375, 0.3403628530427599],
       [0.1065064246463213, 0.3403628529874368, 1.019888595425709]], dtype='float64');
r4=array([-0.2487515050426681,
       -0.8983553811312619,
       0.1093244894479757], dtype='float64');
t4=array([-1311.73757356515,
       -209.1064313369699,
       1426.079759848925], dtype='float64');
Covr4=array([[8.319715458467096e-07, 1.132593316569509e-07, -2.227147975983335e-07],
       [1.132593318606018e-07, 1.078689371307515e-06, 1.040946400531293e-08],
       [-2.227147975857144e-07, 1.040946408076191e-08, 1.146689546907669e-07]], dtype='float64');
Covt4=array([[3.138256925422054, -0.433047869539938, 0.8869749202716044],
       [-0.4330478688213081, 2.579508403107335, 1.077362217139488],
       [0.8869749206812537, 1.077362216824115, 3.080612618068278]], dtype='float64');
r5=array([1.04257333862561,
       -0.06857290069738638,
       -0.04715130855920455], dtype='float64');
t5=array([-1108.272934864627,
       -406.4232940695745,
       3122.706598551033], dtype='float64');
Covr5=array([[1.039060634780197e-06, 1.56777169004056e-07, -9.717695463807614e-08],
       [1.567771692450749e-07, 1.091345316066053e-06, -5.452145900711402e-07],
       [-9.71769547710097e-08, -5.452145900650136e-07, 3.284383156394927e-07]], dtype='float64');
Covt5=array([[11.92999709217625, -1.659763321274758, 2.16703117054859],
       [-1.65976331852328, 9.483924937414153, 2.336763402857045],
       [2.167031171565406, 2.336763402299464, 5.323905617005767]], dtype='float64');
r6=array([0.02775875581421026,
       -0.6070071447928175,
       -1.020053027289401], dtype='float64');
t6=array([-861.1382159827534,
       770.4182387012132,
       2859.138516646855], dtype='float64');
Covr6=array([[9.206156058791656e-07, -9.867118279845717e-08, -1.639222732758872e-07],
       [-9.867118254467439e-08, 1.376970204282672e-06, -1.96722910853274e-07],
       [-1.639222733127222e-07, -1.967229107897762e-07, 8.486261323259699e-08]], dtype='float64');
Covt6=array([[10.34787522159513, -1.271810143140128, 1.353564107022879],
       [-1.27181014075032, 8.102576291309882, 0.1536374526237187],
       [1.353564107272467, 0.1536374523457066, 3.805715022943356]], dtype='float64');
r7=array([-0.8177027096282311,
       0.1328166843233857,
       0.08316389221496358], dtype='float64');
t7=array([-531.6969181490979,
       354.2507807010446,
       3758.917793642077], dtype='float64');
Covr7=array([[8.907646505788794e-07, 1.313060750936897e-07, 8.061350806849556e-08],
       [1.313060753236268e-07, 1.069812803164789e-06, 3.463454798266071e-07],
       [8.061350814648136e-08, 3.463454798147255e-07, 1.278398367775512e-07]], dtype='float64');
Covt7=array([[16.88078949553471, -2.067100431272639, 0.4987264422324232],
       [-2.067100427357855, 13.37834912714538, 2.032255237491632],
       [0.4987264430518239, 2.032255237395293, 3.633541614502283]], dtype='float64');
r8=array([-0.9867735827528934,
       0.2931494063323808,
       0.4361792598371346], dtype='float64');
t8=array([-579.26560331851,
       290.1573566983672,
       5070.799216607405], dtype='float64');
Covr8=array([[1.138531957184517e-06, 5.746644245253596e-08, 2.49718450769628e-07],
       [5.746644269752609e-08, 1.153816063906399e-06, 4.415326811012163e-07],
       [2.497184508708678e-07, 4.415326810451365e-07, 2.585464921193024e-07]], dtype='float64');
Covt8=array([[30.53125982486234, -3.721432030253035, 0.3224973145406664],
       [-3.72143202314351, 24.62862011665368, 3.892853532933795],
       [0.32249731606315, 3.892853532879632, 6.17402171349252]], dtype='float64');
r9=array([-0.5393700842283843,
       0.09675487963436594,
       1.381702737257041], dtype='float64');
t9=array([-1481.49818797205,
       -232.1777575632036,
       5024.076801291849], dtype='float64');
Covr9=array([[2.109755908268389e-06, 4.673047131508447e-07, 4.871492564868479e-07],
       [4.673047134479766e-07, 2.165237242787909e-06, -9.162719379038929e-08],
       [4.871492564850497e-07, -9.162719387869135e-08, 1.841243471966064e-07]], dtype='float64');
Covt9=array([[32.02420259117908, -4.873429355878794, 1.001140458010731],
       [-4.873429348562808, 24.87501155401813, 6.524561278539287],
       [1.001140460406485, 6.524561278174823, 10.91300681567505]], dtype='float64');
r10=array([-0.418321029602559,
       -0.1588868791956113,
       -0.1586959033898704], dtype='float64');
t10=array([-1132.02979567423,
       679.999779634594,
       5471.728906354734], dtype='float64');
Covr10=array([[7.351128938021449e-06, -1.537766661322874e-06, 5.058917965849759e-07],
       [-1.53776666111308e-06, 5.081747782976444e-06, -2.192459058473729e-07],
       [5.058917966144417e-07, -2.192459058363157e-07, 1.375152763734347e-07]], dtype='float64');
Covt10=array([[36.51125626554705, -4.939539874556152, 1.140169175935428],
       [-4.939539866049939, 29.980145563367, 6.569657030536735],
       [1.140169177736126, 6.569657030171525, 17.86529582614892]], dtype='float64');
r11=array([0.567211385989386,
       -0.1058102669603598,
       0.02622320198976105], dtype='float64');
t11=array([-1082.960539611957,
       573.0571031019821,
       4539.145936347583], dtype='float64');
Covr11=array([[1.788528888508008e-06, 1.677394564029927e-07, -5.713950055031996e-09],
       [1.677394566621886e-07, 1.522916490619168e-06, -5.687560269024592e-07],
       [-5.713950156069356e-09, -5.687560268979686e-07, 2.76437826604547e-07]], dtype='float64');
Covt11=array([[25.07592048472608, -3.181586255011166, 2.134276391023885],
       [-3.181586249160503, 20.24083789874537, 3.390652516443521],
       [2.134276392321524, 3.390652515872381, 10.38786867449101]], dtype='float64');
r12=array([-0.3719388882316373,
       -0.9701601973559071,
       -0.1208382352823912], dtype='float64');
t12=array([-1319.098048828083,
       -33.24961968197869,
       723.8903157041009], dtype='float64');
Covr12=array([[1.031736745406552e-06, 6.623259023350081e-08, -2.327444089031148e-07],
       [6.623259044091015e-08, 1.352454337189018e-06, 7.000482931811242e-08],
       [-2.327444088767288e-07, 7.000482939954781e-08, 1.729265242753182e-07]], dtype='float64');
Covt12=array([[1.459742534306553, -0.239059327974448, 0.1450263376851887],
       [-0.2390593277204149, 1.032804222431259, 0.5565891692037876],
       [0.1450263378839813, 0.5565891689994704, 2.866360956421751]], dtype='float64');
r13=array([-0.3576259257376145,
       0.9817295419948378,
       -0.03345493739677603], dtype='float64');
t13=array([602.7042725993218,
       231.4705432359004,
       3188.276281622239], dtype='float64');
Covr13=array([[1.366821693835121e-06, 1.606107039248316e-07, 9.800416389573946e-08],
       [1.606107041439171e-07, 1.557347084633235e-06, 1.429420234768525e-08],
       [9.800416390464173e-08, 1.429420225820513e-08, 2.975159983307725e-07]], dtype='float64');
Covt13=array([[12.38248701793089, -1.530409649229865, -2.553969244995797],
       [-1.53040964637094, 9.978512840967168, 2.517117563046713],
       [-2.553969244304834, 2.517117563710923, 5.077382974213937]], dtype='float64');
r14=array([-0.852059057223485,
       0.7613751330361389,
       1.163096240220191], dtype='float64');
t14=array([838.1627399576039,
       898.7384086794536,
       4201.978980766738], dtype='float64');
Covr14=array([[1.418896893237337e-06, 1.993082844620032e-07, 5.137252050102493e-07],
       [1.993082847093022e-07, 1.499928601339523e-06, 2.281265417358967e-07],
       [5.137252050585682e-07, 2.281265416281992e-07, 3.097095535655793e-07]], dtype='float64');
Covt14=array([[21.71966219083831, -3.29000420431191, -6.271091070368754],
       [-3.290004199244353, 17.73655243436404, 2.825233016495529],
       [-6.271091069606594, 2.825233018019062, 7.696107946500245]], dtype='float64');
r15=array([-1.1042049185949,
       0.4662412920825411,
       0.5137290266966518], dtype='float64');
t15=array([1608.634325493515,
       630.96979609629,
       4021.966279128117], dtype='float64');
Covr15=array([[1.352913103119059e-06, 1.14916377087773e-07, 2.544109325084297e-07],
       [1.149163773197382e-07, 2.122951899290598e-06, 9.957472835201418e-08],
       [2.544109326260653e-07, 9.957472833899211e-08, 6.560658898349766e-07]], dtype='float64');
Covt15=array([[20.96318499198037, -2.526578870931964, -7.028672290608658],
       [-2.526578866141209, 17.61783015158084, 6.205083682957965],
       [-7.028672289334734, 6.205083685426168, 19.54218680205713]], dtype='float64');
r16=array([-0.5817739477302637,
       0.8232790623766272,
       0.4732417114358395], dtype='float64');
t16=array([960.6112431283465,
       130.1378174624314,
       2862.661814714883], dtype='float64');
Covr16=array([[1.424420613201453e-06, -8.164825229920537e-08, 3.079918502070055e-07],
       [-8.164825209387702e-08, 1.825798770020243e-06, 1.416602129708135e-07],
       [3.079918502588968e-07, 1.416602128961827e-07, 2.529608639393951e-07]], dtype='float64');
Covt16=array([[10.15164354675396, -1.257328618927377, -3.916270246003203],
       [-1.257328616542595, 8.402165051668856, 2.6851509621762],
       [-3.916270245250502, 2.685150963093796, 4.937078578239261]], dtype='float64');
r17=array([0.04154853359758953,
       1.437053907625454,
       0.08103214877372231], dtype='float64');
t17=array([750.2073238772522,
       -120.5167422866579,
       2146.085892511522], dtype='float64');
Covr17=array([[1.095009092287593e-06, 2.285662592155612e-07, 4.927635301588569e-07],
       [2.285662594365117e-07, 1.387552439537159e-06, -1.348942179247427e-08],
       [4.927635301229493e-07, -1.348942193341338e-08, 3.485635019337704e-07]], dtype='float64');
Covt17=array([[5.931821883662495, -0.7328128249907878, -1.96417882937109],
       [-0.7328128236263508, 4.705726544395892, 1.72500778469347],
       [-1.964178828878403, 1.725007785162667, 2.90751456881956]], dtype='float64');
r18=array([0.0111143709323448,
       1.382486148397389,
       -0.002383298003564256], dtype='float64');
t18=array([490.492903797177,
       -75.19723854252284,
       2356.237114731608], dtype='float64');
Covr18=array([[7.925266892904134e-07, 1.980931892931684e-07, 3.953874838050566e-07],
       [1.980931895176451e-07, 1.161486420321007e-06, -6.217368620443878e-09],
       [3.9538748377612e-07, -6.2173687599347e-09, 2.874772480257451e-07]], dtype='float64');
Covt18=array([[6.818299004712578, -0.8606776635975076, -1.581916092919276],
       [-0.8606776620407514, 5.28345114890609, 1.358335843503642],
       [-1.581916092494591, 1.358335843845747, 1.736394105508165]], dtype='float64');
r19=array([0.006127992521635144,
       1.20511213402959,
       -0.01096792821034782], dtype='float64');
t19=array([-329.8340523648138,
       12.79464088894334,
       2400.831708945108], dtype='float64');
Covr19=array([[8.610591969337531e-07, 2.050683683373193e-07, 3.844965789838351e-07],
       [2.050683685812251e-07, 1.223593913294701e-06, 2.062319026579011e-09],
       [3.84496578957398e-07, 2.062318878243945e-09, 3.404960570181008e-07]], dtype='float64');
Covt19=array([[6.864432675192579, -0.8237674725235169, 0.5223563233291433],
       [-0.8237674709636572, 5.286635069210184, 0.5761999674852053],
       [0.522356323578224, 0.5761999673558489, 0.7317310821205212]], dtype='float64');
r20=array([-0.5249448286909882,
       -0.2742365960487252,
       0.02954406219540435], dtype='float64');
t20=array([-1604.996733510909,
       310.193138640245,
       2018.945705154997], dtype='float64');
Covr20=array([[4.239684629667139e-06, 8.4811081580258e-07, 4.52340211388518e-07],
       [8.48110815964231e-07, 3.45838343298905e-06, 1.51476809813112e-07],
       [4.523402114195528e-07, 1.514768098171213e-07, 1.19724865304452e-07]], dtype='float64');
Covt20=array([[5.503203277258351, -0.8819675333145142, 1.733283537417455],
       [-0.8819675319896265, 5.156329015098371, 1.744379608644617],
       [1.733283537823231, 1.744379608028384, 6.36788565954119]], dtype='float64');
