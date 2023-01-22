#include <vector> 
std::vector<std::vector<double>> path = { 
{5.478394239583333, 1.3908658645833334, 0, 0},
{5.4779497500000005, 1.4065894166666666, 0.25083726576083964, 0.08898137532890503},
{5.477829885416667, 1.42217209375, 0.3539094322530274, 0.16754171067246215},
{5.478031333333334, 1.4376153333333332, 0.4324697675965845, 0.23335530361132995},
{5.47855078125, 1.4529205729166668, 0.4982833605354523, 0.29099701515682597},
{5.479384916666667, 1.46808925, 0.5559250720809483, 0.3428228872858876},
{5.480530427083334, 1.4831228020833334, 0.60775094421001, 0.3902387972259517},
{5.481984000000001, 1.4980226666666667, 0.655166854150074, 0.43416514501376435},
{5.483742322916667, 1.51279028125, 0.6990932019378867, 0.47524448367807537},
{5.485802083333334, 1.5274270833333334, 0.7401725406021976, 0.5139471284536086},
{5.48815996875, 1.5419345104166666, 0.7788751853777307, 0.5506300664941876},
{5.490812666666667, 1.556314, 0.8155581234183098, 0.5855721804679034},
{5.493756864583333, 1.5705669895833334, 0.8505002373920256, 0.6189964858090563},
{5.49698925, 1.5846949166666666, 0.8839245427331787, 0.6510847976542992},
{5.500506510416667, 1.59869921875, 0.9160128545784215, 0.681987759972621},
{5.504305333333334, 1.6125813333333334, 0.9469158168967433, 0.7118319142097722},
{5.50838240625, 1.6263426979166666, 0.9767599711338946, 0.7407248115941145},
{5.5127344166666665, 1.63998475, 1.0056528685182369, 0.7687587938805056},
{5.517358052083334, 1.6535089270833334, 1.033686850804628, 0.7960138443310261},
{5.52225, 1.6669166666666668, 1.0609419012551484, 0.8225597748469109},
{5.527406947916667, 1.6802094062500001, 1.0874878317710333, 0.8484579297093606},
{5.5328255833333335, 1.6933885833333333, 1.113385986633483, 0.8697154314543937},
{5.53850259375, 1.706455635416667, 1.1386905880614575, 0.8449562073269746},
{5.544434666666667, 1.7194120000000002, 1.1634498121888768, 0.820699360240876},
{5.550618489583333, 1.7322591145833335, 1.1877066592749754, 0.7969063546732079},
{5.55705075, 1.7449984166666668, 1.2114996648426435, 0.7735425331094911},
{5.5637281354166666, 1.75763134375, 1.2348634864063603, 0.7505766276596507},
{5.5706473333333335, 1.7701593333333334, 1.2578293918562007, 0.7279803501811569},
{5.5778050312500005, 1.7825838229166668, 1.2804256693346945, 0.7057280456482639},
{5.585197916666667, 1.7949062500000001, 1.3026779738675875, 0.6837963969085784},
{5.592822677083333, 1.8071280520833335, 1.324609622607273, 0.662164171526399},
{5.600676, 1.8192506666666668, 1.3462418479894525, 0.640812003355793},
{5.608754572916666, 1.8312755312500002, 1.3675940161600586, 0.6197222029770534},
{5.617055083333334, 1.8432040833333336, 1.388683816538798, 0.5988785922836394},
{5.62557421875, 1.8550377604166668, 1.409527427232212, 0.5782663594065224},
{5.634308666666667, 1.866778, 1.430139660109329, 0.5578719308702605},
{5.643255114583334, 1.8784262395833335, 1.4505340886455909, 0.5376828584350767},
{5.65241025, 1.889983916666667, 1.4707231610807747, 0.5176877185255487},
{5.661770760416667, 1.90145246875, 1.4907183009903027, 0.4978760225044562},
{5.671333333333333, 1.9128333333333334, 1.5105299970113955, 0.47823813633903656},
{5.68109465625, 1.9241279479166669, 1.530167883176815, 0.4587652084412138},
{5.691051416666666, 1.9353377500000002, 1.5496408110746378, 0.43944910465438236},
{5.7012003020833335, 1.9464641770833335, 1.5689569148614693, 0.4202823495160347},
{5.711538, 1.957508666666667, 1.5881236699998171, 0.40125807305455574},
{5.722061197916667, 1.9684726562500003, 1.607147946461296, 0.38236996248542143},
{5.732766583333333, 1.9793575833333334, 1.6260360570304302, 0.3636122182609066},
{5.74365084375, 1.990164885416667, 1.644793801254945, 0.34497951400174764},
{5.754710666666667, 2.0008960000000005, 1.663426505514104, 0.3264669599015505},
{5.765942739583333, 2.0115523645833333, 1.6819390596143011, 0.3080700692473558},
{5.77734375, 2.022135416666667, 1.7003359502684958, 0.2897847277443416},
{5.788910385416667, 2.03264659375, 1.71862129177151, 0.2716071653705082},
{5.800639333333334, 2.0430873333333337, 1.7367988541453434, 0.25353393051962214},
{5.81252728125, 2.0534590729166666, 1.7548720889962293, 0.23556186621843944},
{5.824570916666667, 2.06376325, 1.772844153297412, 0.21768808822819363},
{5.836766927083334, 2.0740013020833334, 1.7907179312876578, 0.19990996486102663},
{5.849112, 2.0841746666666667, 1.8084960546548248, 0.18222509836001854},
{5.861602822916667, 2.0942847812500003, 1.8261809211558329, 0.1646313077071785},
{5.874236083333334, 2.1043330833333336, 1.843774711808673, 0.1471266127374461},
{5.88700846875, 2.114321010416667, 1.8612794067784053, 0.12970921944883507},
{5.899916666666667, 2.1242500000000004, 1.8786968000670161, 0.11237750640946309},
{5.912957364583334, 2.134121489583334, 1.896028513106388, 0.09513001217160977},
{5.92612725, 2.143936916666667, 1.9132760073442414, 0.07796542361128489},
{5.939423010416667, 2.15369771875, 1.930440595904566, 0.060882565119212084},
{5.952841333333334, 2.1634053333333334, 1.9475234543966387, 0.04388038857575405},
{5.96637890625, 2.1730611979166667, 1.9645256309400967, 0.026957964048239247},
{5.980032416666667, 2.18266675, 1.9814480554676115, 0.010114471154471949},
{5.993798552083334, 2.1922234270833334, 1.9982915483613788, -0.006650808959011267},
{6.007674000000001, 2.201732666666667, 2.015056828474862, -0.02333850107104618},
{6.021655447916667, 2.2111959062500004, 2.031744520586897, -0.03994914281552997},
{6.035739583333334, 2.2206145833333335, 2.0483551623313807, -0.05648319112636668},
{6.04992309375, 2.229990135416667, 2.0648892106422174, -0.07294102823415505},
{6.0642026666666675, 2.2393240000000003, 2.081347047750006, -0.08932296724818112},
{6.078574989583334, 2.248617614583334, 2.097728986764032, -0.10562925735464057},
{6.0930367500000004, 2.2578724166666673, 2.1140352768704913, -0.1218600886595892},
{6.107584635416667, 2.2670898437500004, 2.13026610817544, -0.13801559670292407},
{6.122215333333334, 2.2762713333333338, 2.146421616218775, -0.1540958666676845},
{6.136925531250001, 2.285418322916667, 2.162501886183535, -0.17010093730712084},
{6.151711916666667, 2.2945322500000005, 2.178506956822971, -0.18603080461029398},
{6.166571177083334, 2.3036145520833338, 2.1944368241261443, -0.2018854252254062},
{6.181500000000001, 2.312666666666667, 2.210291444741257, -0.21766471965868728},
{6.196495072916667, 2.32169003125, 2.2260707391745385, -0.23336857526530996},
{6.211553083333334, 2.330686083333334, 2.241774594781161, -0.24899684904764097},
{6.22667071875, 2.339656260416667, 2.2574028685634926, -0.2645493702750493},
{6.241844666666667, 2.3486020000000005, 2.272955389790901, -0.2800259429384305},
{6.257071614583334, 2.357524739583334, 2.288431962454282, -0.2954263480517393},
{6.272348250000001, 2.366425916666667, 2.3038323675675905, -0.3107503458119235},
{6.287671260416667, 2.3753069687500004, 2.3191563653277747, -0.32599767762788356},
{6.303037333333334, 2.384169333333334, 2.3344036971437343, -0.3411680680283412},
{6.318443156250001, 2.3930144479166673, 2.349574087544192, -0.3562612264578585},
{6.333885416666668, 2.4018437500000003, 2.3646672459737093, -0.371276848969602},
{6.349360802083334, 2.410658677083334, 2.3796828684854527, -0.3862146198229034},
{6.364866000000001, 2.419460666666667, 2.3946206393387546, -0.4010742129931274},
{6.380397697916667, 2.4282511562500004, 2.409480232508979, -0.4158552936008978},
{6.395952583333334, 2.437031583333334, 2.4242613131167494, -0.43055751926725694},
{6.411527343750001, 2.445803385416667, 2.438963538783109, -0.44518054140096674},
{6.427118666666668, 2.4545680000000005, 2.453586560916819, -0.45972400642374855},
{6.4427232395833345, 2.4633268645833337, 2.4681300259396, -0.47418755693892833},
{6.458337750000001, 2.472081416666667, 2.48259357645478, -0.48857083284864167},
{6.473958885416668, 2.4808330937500003, 2.4969768523644933, -0.5028734724244507},
{6.489583333333334, 2.489583333333334, 2.5112794919403023, -0.4886518315129392},
{6.505207781250001, 2.498333572916667, 2.5255011328518138, -0.47451155120710975},
{6.520828916666668, 2.5070852500000003, 2.5396414131576432, -0.46045299210190416},
{6.536443427083334, 2.5158398020833337, 2.553699972262849, -0.4464765125180129},
{6.552048000000001, 2.524598666666667, 2.56767645184674, -0.432582467599952},
{6.567639322916667, 2.5333632812500007, 2.581570496764801, -0.4187712084364773},
{6.583214083333335, 2.542135083333334, 2.5953817559282757, -0.4050430811999298},
{6.598768968750001, 2.550915510416667, 2.609109883164823, -0.3913984263012428},
{6.614300666666668, 2.5597060000000007, 2.62275453806351, -0.37783757755749015},
{6.629805864583335, 2.568507989583334, 2.6363153868072633, -0.36436086136893653},
{6.645281250000001, 2.577322916666667, 2.649792102995817, -0.35096859590267504},
{6.660723510416668, 2.5861522187500006, 2.6631843684620784, -0.33763535310949944},
{6.676129333333335, 2.5949973333333336, 2.6661846922404298, -0.32429563160128205},
{6.691495406250001, 2.6038596979166675, 2.6528449707322124, -0.3109096527367109},
{6.7068184166666684, 2.6127407500000004, 2.639458991867641, -0.2974782766189906},
{6.7220950520833345, 2.621641927083334, 2.6260276157499205, -0.2840023629179237},
{6.737322000000002, 2.6305646666666673, 2.6125517020488536, -0.27048276973143304},
{6.752495947916668, 2.6395104062500003, 2.599032108862363, -0.25692035237680366},
{6.767613583333334, 2.648480583333334, 2.5854696915077335, -0.24331596210627449},
{6.782671593750001, 2.6574766354166672, 2.5718653012372044, -0.2296704447412944},
{6.797666666666668, 2.666500000000001, 2.5582197838722243, -0.21598463921946676},
{6.812595489583335, 2.675552114583334, 2.5445339783503966, -0.20225937604786492},
{6.827454750000002, 2.6846344166666674, 2.5308087151787944, -0.1884954756560865},
{6.842241135416668, 2.6937483437500007, 2.517044814787016, -0.1746937466420192},
{6.856951333333335, 2.702895333333334, 2.5032430857729486, -0.16085498390295505},
{6.871582031250002, 2.7120768229166674, 2.4894043230338845, -0.14697996664425206},
{6.886129916666668, 2.7212942500000006, 2.4755293057751815, -0.13306945625736277},
{6.900591677083335, 2.7305490520833344, 2.4616187953882926, -0.11912419405860175},
{6.914964000000001, 2.739842666666667, 2.447673533189531, -0.10514489887956813},
{6.929243572916668, 2.7491765312500007, 2.4336942380104976, -0.0911322644996958},
{6.943427083333335, 2.7585520833333343, 2.4196816036306252, -0.07708695691087575},
{6.9575112187500014, 2.7679707604166675, 2.405636296041805, -0.0630096114036428},
{6.971492666666668, 2.777434000000001, 2.3915589505345722, -0.04890082946385588},
{6.985368114583335, 2.7869432395833345, 2.3774501685947853, -0.034761175468292715},
{6.999134250000001, 2.7964999166666673, 2.363310514599222, -0.02059117316701442},
{7.012787760416668, 2.8061054687500007, 2.349140512297944, -0.006391301939818628},
{7.026325333333334, 2.8157613333333344, 2.334940641070748, 0.007838007186511953},
{7.0397436562500015, 2.8254689479166677, 2.3207113319444175, 0.02209637577399637},
{7.053039416666668, 2.8352297500000008, 2.306452963356933, 0.036383482476730955},
{7.066209302083335, 2.8450451770833345, 2.2921658566541985, 0.05069906782666733},
{7.079250000000002, 2.8549166666666674, 2.277850271304262, 0.06504293931752791},
{7.092158197916668, 2.864845656250001, 2.2635063998134015, 0.0794149768030562},
{7.104930583333335, 2.8748335833333343, 2.2491343623278732, 0.09381513822639687},
{7.117563843750002, 2.8848818854166676, 2.2347342009045326, 0.10824346569796417},
{7.130054666666668, 2.894992000000001, 2.2203058734329653, 0.12270009193972531},
{7.142399739583335, 2.9051653645833344, 2.205849247191204, 0.13718524711434432},
{7.154595750000002, 2.9154034166666674, 2.191364092016585, 0.15169926605817763},
{7.166639385416668, 2.925707593750001, 2.176850073072752, 0.16624259593757984},
{7.178527333333335, 2.9360793333333346, 2.1623067431933496, 0.18081580434845324},
{7.190256281250001, 2.946520072916668, 2.147733534782476, 0.19541958787942104},
{7.201822916666669, 2.957031250000001, 2.1331297512515084, 0.2100547811593746},
{7.213223927083336, 2.9676143020833345, 2.118494557971555, 0.22472236641056853},
{7.224456000000002, 2.9782706666666674, 2.103826972720361, 0.23942348352874776},
{7.2355158229166685, 2.9890017812500007, 2.0891258556021817, 0.25415944071213803},
{7.246400083333335, 2.9998090833333344, 2.0743898984187914, 0.26893172566147394},
{7.257105468750002, 3.0106940104166675, 2.059617613469456, 0.2837420173735611},
{7.267628666666669, 3.021658000000001, 2.044807321757369, 0.2985921985512384},
{7.277966364583334, 3.0327024895833343, 2.0299571405796915, 0.31348436865307516},
{7.288115250000002, 3.0438289166666674, 2.0150649704778547, 0.3284208576066373},
{7.298072010416668, 3.055038718750001, 2.0001284815242926, 0.34340424020992144},
{7.307833333333336, 3.0663333333333345, 1.9851450989210089, 0.35843735124641685},
{7.3173959062500025, 3.0777141979166673, 1.9701119878845137, 0.3735233013405682},
{7.326756416666669, 3.089182750000001, 1.955026037790362, 0.3886654935819892},
{7.335911552083335, 3.100740427083335, 1.939883845548941, 0.4038676409489984},
{7.344858000000001, 3.112388666666668, 1.924681698181932, 0.4191337845648958},
{7.353592447916668, 3.124128906250001, 1.9094155545660345, 0.4344683128240786},
{7.362111583333335, 3.1359625833333347, 1.8940810263068517, 0.4498759814299019},
{7.3704120937500015, 3.1478911354166677, 1.8786733577010284, 0.4653619343922354},
{7.378490666666669, 3.159916000000001, 1.8631874047386947, 0.48093172604032175},
{7.386343989583336, 3.172038614583334, 1.8476176130906083, 0.4965913441161375},
{7.393968750000002, 3.1842604166666675, 1.8319579950147928, 0.5123472340253185},
{7.401361635416668, 3.1965828437500012, 1.8162021051056119, 0.5282063243373064},
{7.408519333333335, 3.209007333333335, 1.800343014793624, 0.5441760536442507},
{7.415438531250002, 3.221535322916668, 1.7843732854866796, 0.5602643989098431},
{7.422115916666668, 3.2341682500000015, 1.7682849402210872, 0.5764799054654214},
{7.428548177083336, 3.246907552083335, 1.752069433665509, 0.5928317188420801},
{7.434732000000002, 3.2597546666666677, 1.73571762028885, 0.6093296186651004},
{7.440664072916667, 3.2727110312500014, 1.7192197204658297, 0.625984054881697},
{7.446341083333334, 3.2857780833333345, 1.7025652842492331, 0.6428061866462699},
{7.451759718750001, 3.298957260416668, 1.6857431524846602, 0.659807924250318},
{7.456916666666668, 3.312250000000001, 1.6687414148806121, 0.6770019745587709},
{7.461808614583335, 3.3256577395833347, 1.6515473645721594, 0.6944018905028037},
{7.466432250000002, 3.339181916666668, 1.6341474486281264, 0.7120221252838063},
{7.470784260416669, 3.352823968750001, 1.6165272138471236, 0.7298780920672684},
{7.474861333333334, 3.366585333333335, 1.5986712470636615, 0.7479862300929631},
{7.478660156250001, 3.3804674479166685, 1.5805631090379668, 0.7663640783039966},
{7.4821774166666675, 3.394471750000002, 1.5621852608269335, 0.7850303578084624},
{7.485409802083335, 3.408599677083335, 1.5435189813224677, 0.8040050647418747},
{7.488354000000001, 3.4228526666666683, 1.5245442743890554, 0.8233095754068743},
{7.491006697916668, 3.4372321562500017, 1.5052397637240555, 0.8429667659427663},
{7.493364583333335, 3.4517395833333353, 1.4855825731881638, 0.8630011492393043},
{7.495424343750001, 3.4663763854166687, 1.4655481898916258, 0.8834390323806948},
{7.497182666666667, 3.481144000000002, 1.4451103067502353, 0.9043086986185852},
{7.498636239583334, 3.496043864583335, 1.424240640512345, 0.9256406187691729},
{7.49978175, 3.5110774166666685, 1.4029087203617572, 0.9474676980664493},
{7.500615885416668, 3.5262460937500015, 1.3810816410644808, 0.9698255659585097},
{7.501135333333334, 3.5415513333333353, 1.3587237731724204, 0.9927529182132383},
{7.501336781250001, 3.5569945729166683, 1.3357964209176922, 1.0162919231514165},
{7.501216916666668, 3.5725772500000015, 1.312257415979514, 1.0404887070569382},
{7.500772427083334, 3.5883008020833356, 1.2880606320739927, 1.0653939381208533},
{7.500000000000001, 3.604166666666668, 1.2631554010100778, 1.0910096575686392},
{7.498855380208333, 3.620139984375, 1.2375396815622919, 1.1168398633332686},
{7.497299291666667, 3.6361844583333336, 1.2587248622711558, 1.1424078896571075},
{7.495335890625, 3.652299369791667, 1.281022024568685, 1.1677137355089275},
{7.492969333333333, 3.6684840000000003, 1.30442596887707, 1.1927573992473217},
{7.490203776041667, 3.6847376302083337, 1.3289317791780064, 1.2175464002928944},
{7.487043375, 3.701059541666667, 1.3537207802235793, 1.2420995474710894},
{7.4834922864583335, 3.717449015625, 1.3782739274017748, 1.2664383350074813},
{7.479554666666667, 3.7339053333333334, 1.4026127149381664, 1.290582042003848},
{7.475234671875, 3.750427776041667, 1.4267564219345334, 1.2702808554945477},
{7.470536458333333, 3.7670156250000004, 1.4507223440350816, 1.2464772023686752},
{7.465464182291667, 3.7836681614583334, 1.4745259971609543, 1.222821902059728},
{7.460022, 3.800384666666667, 1.4981812974699011, 1.1993024785970912},
{7.4542140677083335, 3.8171644218750003, 1.5217007209325382, 1.1759077542135516},
{7.4480445416666665, 3.834006708333334, 1.5450954453160775, 1.1526277226381154},
{7.441517578125, 3.850910807291667, 1.568375476891514, 1.1294534357277266},
{7.434637333333333, 3.8678760000000003, 1.5915497638019027, 1.1063769018041478},
{7.4274079635416665, 3.884901567708334, 1.6146262977254813, 1.0833909943081812},
{7.419833625, 3.901986791666667, 1.637612205221448, 1.0604893695840607},
{7.411918473958333, 3.9191309531250003, 1.6605138299455682, 1.0376663927718468},
{7.403666666666667, 3.9363333333333337, 1.6833368067577819, 1.0149170709223574},
{7.395082359375, 3.953593213541667, 1.706086128607271, 0.9922369925633951},
{7.386169708333333, 3.9709098750000003, 1.728766206966233, 0.9696222730420905},
{7.376932869791666, 3.988282598958334, 1.7513809264875377, 0.9470695050496358},
{7.367376, 4.005710666666667, 1.7739336944799924, 0.9245757138041748},
{7.357503255208333, 4.023193359375, 1.796427485725453, 0.9021383164273153},
{7.347318791666667, 4.040729958333333, 1.8188648831023122, 0.8797550851013058},
{7.336826765625, 4.0583197447916675, 1.8412481144283215, 0.8574241136387544},
{7.326031333333333, 4.0759620000000005, 1.8635790858908725, 0.8351437871358911},
{7.314936651041666, 4.0936560052083335, 1.8858594123937358, 0.8129127544147465},
{7.303546874999999, 4.111401041666667, 1.9080904451148804, 0.7907299029898667},
{7.2918661614583336, 4.129196390625, 1.9302732965397602, 0.7685943363219181},
{7.279898666666666, 4.147041333333334, 1.952408863207709, 0.7465053531443253},
{7.267648546875, 4.164935151041667, 1.9744978463853018, 0.7244624286701278},
{7.255119958333333, 4.182877125000001, 1.9965407708594993, 0.7024651975051555},
{7.242317057291666, 4.200866536458334, 2.018538002024471, 0.6805134381103963},
{7.229244, 4.218902666666668, 2.0404897614192303, 0.6586070586715529},
{7.215904942708333, 4.236984796875, 2.0623961408580733, 0.6367460842472985},
{7.202304041666666, 4.255112208333334, 2.0842571152823273, 0.6149306450799132},
{7.1884454531249995, 4.273284182291667, 2.1060725544497125, 0.593160965962908},
{7.174333333333333, 4.291500000000001, 2.1278422335667178, 0.5714373565701223},
{7.159971838541666, 4.309758942708334, 2.1495658429595035, 0.5497602026596544},
{7.145365125, 4.3280602916666675, 2.1712429968699714, 0.528129958074004},
{7.130517348958333, 4.3464033281250005, 2.1928732414556213, 0.5065471374650743},
{7.115432666666666, 4.364787333333334, 2.2144560620645506, 0.48501230967920606},
{7.100115234375, 4.383211588541667, 2.235990889850419, 0.4635260917433577},
{7.084569208333333, 4.401675375000001, 2.257477107786267, 0.44208914339892047},
{7.068798744791666, 4.420177973958334, 2.2789140561307044, 0.4207021621344813},
{7.052808, 4.438718666666667, 2.300301037395144, 0.399365878673283},
{7.036601130208333, 4.457296734375001, 2.3216373208563423, 0.37808105287511484},
{7.020182291666666, 4.475911458333334, 2.342922146654511, 0.356848470015958},
{7.003555640625, 4.494562119791667, 2.364154729513668, 0.33566893741203785},
{6.986725333333333, 4.513248000000001, 2.385334262117588, 0.3145432813578779},
{6.969695526041666, 4.531968380208334, 2.4064599181717483, 0.29347234435067815},
{6.952470375, 4.5507225416666675, 2.4275308551789485, 0.272456982575787},
{6.935054036458332, 4.569509765625001, 2.44854621695384, 0.25149806363028393},
{6.917450666666666, 4.588329333333334, 2.4695051358993427, 0.2305964644636953},
{6.899664421874999, 4.607180526041668, 2.490406735065931, 0.20975306951674177},
{6.881699458333332, 4.626062625000001, 2.511250130012884, 0.18896876904067028},
{6.8635599322916665, 4.644974911458334, 2.532034430488956, 0.16824445758125695},
{6.845249999999999, 4.663916666666667, 2.5527587419483693, 0.1475810326129796},
{6.826773817708332, 4.6828871718750005, 2.573422166916646, 0.12697939331007913},
{6.808135541666666, 4.701885708333334, 2.594023806219546, 0.10644043944242298},
{6.789339328124999, 4.720911557291668, 2.6145627600872023, 0.08596507038511625},
{6.770389333333332, 4.7399640000000005, 2.6350381291445095, 0.06555418423175219},
{6.751289713541666, 4.759042317708334, 2.655449015297874, 0.04520867700209408},
{6.7320446249999994, 4.778145791666668, 2.675794522527532, 0.024929441935736207},
{6.712658223958332, 4.797273703125001, 2.6960737575938896, 0.00471736886405516},
{6.693134666666666, 4.816425333333335, 2.7162858306655706, -0.015426656346610557},
{6.673478109374999, 4.835599963541668, 2.7364298558762363, -0.03550175228699359},
{6.653692708333333, 4.854796875000001, 2.7565049518166194, -0.055507042438031284},
{6.633782619791666, 4.874015348958334, 2.776510241967657, -0.0754416555505033},
{6.613751999999999, 4.893254666666667, 2.796444855080129, -0.0953047259761064},
{6.593605005208333, 4.912514109375001, 2.8163079255057326, -0.11509539395448609},
{6.573345791666666, 4.931792958333334, 2.8360985934841123, -0.13481280586035904},
{6.552978515624999, 4.951090494791668, 2.8558160053899857, -0.15445611441451756},
{6.532507333333332, 4.970406000000001, 2.875459313944144, -0.17402447886218742},
{6.511936401041666, 4.989738755208334, 2.895027678391813, -0.1935170651219238},
{6.491269874999999, 5.009088041666668, 2.914520264651549, -0.2129330459079446},
{6.470511911458332, 5.028453140625001, 2.9339362454375704, -0.232271600828601},
{6.4496666666666655, 5.047833333333335, 2.9532748003582263, -0.2515319164634082},
{6.428738296874998, 5.067227901041668, 2.972535115993034, -0.27071318642091136},
{6.407730958333332, 5.086636125000002, 2.991716385950537, -0.2898146113794313},
{6.386648807291666, 5.106057286458334, 3.010817810909057, -0.30883539911260804},
{6.3654959999999985, 5.125490666666668, 3.0298385986422334, -0.3277747645014628},
{6.344276692708332, 5.1449355468750015, 3.048777964031088, -0.3466319295346052},
{6.322995041666665, 5.164391208333335, 3.0676351290642305, -0.365406123298043},
{6.301655203124999, 5.183856932291668, 3.0864093228276688, -0.38409658195596386},
{6.280261333333332, 5.203332000000001, 3.1050997814855896, -0.40270254872373545},
{6.258817588541666, 5.222815692708335, 3.1237057482533612, -0.4212232738342889},
{6.237328124999999, 5.242307291666668, 3.1422264733639147, -0.43965801449894304},
{6.2157970989583315, 5.261806078125002, 3.160661214028569, -0.45800603486366587},
{6.194228666666666, 5.281311333333335, 3.179009234393292, -0.47626660596169224},
{6.172626984374999, 5.300822338541668, 3.197269805491318, -0.49445675498824926},
{6.150996208333332, 5.320338375000001, 3.209184900269331, -0.5126782068468563},
{6.129340494791665, 5.339858723958335, 3.1909634484107245, -0.5310155573184643},
{6.107663999999999, 5.359382666666668, 3.1726260979391165, -0.5494685668411119},
{6.085970880208332, 5.378909484375002, 3.154173088416469, -0.568037001702578},
{6.064265291666665, 5.3984384583333345, 3.135604653555003, -0.5867206344628304},
{6.042551390624999, 5.417968869791668, 3.11692102079475, -0.6055192443934416},
{6.020833333333332, 5.437500000000002, 3.0981224108641383, -0.5866058708512352},
{5.999115276041666, 5.4570311302083345, 3.079209037321932, -0.5675779396080687},
{5.977401374999999, 5.476561541666668, 3.0601811060787654, -0.5484356484257127},
{5.955695786458332, 5.496090515625002, 3.0410388148964094, -0.5291791863920743},
{5.9340026666666645, 5.515617333333335, 3.0217823528627705, -0.5098087333698267},
{5.912326171874998, 5.535141276041669, 3.0024118998405234, -0.49032445941642333},
{5.890670458333332, 5.554661625000001, 2.9829276258871205, -0.47072652417307204},
{5.869039682291665, 5.574177661458335, 2.9633296906437696, -0.4510150762201288},
{5.847437999999998, 5.593688666666669, 2.9436182426908264, -0.4311902523961262},
{5.825869567708331, 5.613193921875002, 2.9237934188668238, -0.4112521770775013},
{5.804338541666665, 5.632692708333336, 2.9038553435481993, -0.3912009614158505},
{5.782849078124998, 5.652184307291669, 2.883804127886548, -0.3710367025292882},
{5.7614053333333315, 5.671668000000002, 2.8636398689999862, -0.3507594826442455},
{5.740011463541665, 5.691143067708335, 2.843362649114944, -0.3303693681837432},
{5.718671624999998, 5.710608791666669, 2.8229725346544416, -0.30986640879786354},
{5.697389973958332, 5.730064453125001, 2.8024695752685624, -0.28925063633180237},
{5.676170666666665, 5.749509333333335, 2.7818538028025017, -0.26852206372651377},
{5.655017859374998, 5.768942713541668, 2.761125230197213, -0.2476806838465171},
{5.633935708333332, 5.788363875000002, 2.7402838503172164, -0.22672646822902376},
{5.612928369791665, 5.807772098958335, 2.719329634699723, -0.20565936574801214},
{5.591999999999999, 5.827166666666669, 2.6982625322187115, -0.18447930118634304},
{5.571154755208331, 5.846546859375001, 2.677082467657042, -0.16318617370840283},
{5.550396791666665, 5.865911958333335, 2.6557893401791013, -0.14177985522510372},
{5.529730265624998, 5.885261244791669, 2.634383021695802, -0.12026018864233468},
{5.509159333333331, 5.904594000000001, 2.6128633551130327, -0.098626985983155},
{5.488688151041664, 5.923909505208336, 2.5912301524538535, -0.07688002637314106},
{5.468320874999998, 5.9432070416666685, 2.5694831928438395, -0.055019053877289004},
{5.448061661458331, 5.962485890625002, 2.547622220347988, -0.03304377517584367},
{5.4279146666666644, 5.981745333333335, 2.525646941646543, -0.010953857065156392},
{5.407884046874998, 6.0009846510416684, 2.5035570235358557, 0.011251076231597601},
{5.3879739583333315, 6.020203125000002, 2.4813520902391017, 0.03357144596051942},
{5.368188557291665, 6.039400036458336, 2.4590317205101795, 0.056007721958221346},
{5.348531999999998, 6.058574666666669, 2.4365954445124776, 0.07856042601831703},
{5.329008442708331, 6.077726296875002, 2.4140427404523823, 0.10123013552534754},
{5.309622041666665, 6.096854208333335, 2.391373030945352, 0.12401748738056817},
{5.290376953124998, 6.115957682291668, 2.3685856790901316, 0.14692318224654954},
{5.271277333333332, 6.135036000000002, 2.3456799842241507, 0.16994798914040565},
{5.252327338541665, 6.1540884427083355, 2.3226551773302946, 0.19309275040858687},
{5.233531124999997, 6.173114291666669, 2.2995104160621134, 0.21635838711976696},
{5.214892848958332, 6.192112828125002, 2.2762447793509337, 0.23974590491633485},
{5.196416666666664, 6.211083333333335, 2.2528572615543654, 0.2632564003694853},
{5.178106734374998, 6.230025088541669, 2.229346766101215, 0.2868910678879919},
{5.159967208333331, 6.248937375000002, 2.205712098582709, 0.31065120723645556},
{5.142002244791664, 6.267819473958335, 2.1819519592342456, 0.33453823172530583},
{5.124215999999998, 6.2866706666666685, 2.1580649347453953, 0.3585536771421669},
{5.106612630208332, 6.305490234375002, 2.134049489328534, 0.3826992115025485},
{5.0891962916666635, 6.324277458333335, 2.1099039549681526, 0.4069766457073136},
{5.071971140624997, 6.3430316197916685, 2.0856265207633875, 0.43138794520522783},
{5.054941333333332, 6.361752000000003, 2.0612152212654733, 0.4559352427712424},
{5.0381110260416655, 6.380437880208335, 2.0366679236994583, 0.48062085252542186},
{5.021484374999998, 6.399088541666669, 2.011982313945279, 0.5054472853336849},
{5.005065536458331, 6.417703265625002, 1.9871558811370158, 0.530417265750387},
{4.988858666666664, 6.436281333333335, 1.962185900720314, 0.5555337506844422},
{4.9728679218749985, 6.454822026041668, 1.9370694157862582, 0.5807999499958809},
{4.957097458333331, 6.473324625000002, 1.9118032164748195, 0.6062193492589207},
{4.941551432291664, 6.4917884114583355, 1.8863838172117795, 0.6317957349617735},
{4.926233999999997, 6.510212666666669, 1.860807431508927, 0.6575332224531714},
{4.911149317708332, 6.528596671875002, 1.835069944017529, 0.6834362869923849},
{4.896301541666664, 6.546939708333335, 1.8091668794783153, 0.7095097983145031},
{4.881694828124997, 6.565241057291669, 1.783093368156197, 0.7357590591878118},
{4.867333333333331, 6.583500000000003, 1.7568441072828882, 0.7621898485172265},
{4.853221213541665, 6.601715817708335, 1.7304133179534738, 0.7888084696397062},
{4.839362624999998, 6.6198877916666685, 1.7037946968309945, 0.8156218045675088},
{4.8257617239583315, 6.638015203125002, 1.676981361903192, 0.842637375067401},
{4.812422666666665, 6.656097333333335, 1.6499657914033, 0.8698634116235615},
{4.799349609374998, 6.6741334635416685, 1.6227397548471394, 0.8973089315257328},
{4.786546708333331, 6.692122875000003, 1.595294234944968, 0.9249838275607072},
{4.7740181197916645, 6.710064848958336, 1.567619338909993, 0.9528989690754903},
{4.761767999999998, 6.727958666666669, 1.5397041973952101, 0.9810663175388319},
{4.749800505208331, 6.7458036093750025, 1.5115368489318686, 1.0094990591730673},
{4.738119791666664, 6.763598958333335, 1.4831041072976332, 1.0382117577851098},
{4.726730015624998, 6.781343994791669, 1.4543914086855905, 1.0672205316268952},
{4.7156353333333305, 6.799038000000002, 1.425382634843805, 1.0965432590060313},
{4.704839901041664, 6.816680255208335, 1.3960599074646687, 1.1261998185067092},
{4.694347874999998, 6.834270041666668, 1.3664033479639908, 1.1562123711513506},
{4.684163411458332, 6.851806640625003, 1.3363907953193497, 1.186605693748855},
{4.674290666666665, 6.869289333333335, 1.305997472721845, 1.2174075751950886},
{4.664733796874998, 6.886717401041668, 1.275195591275612, 1.2486492908415334},
{4.655496958333331, 6.904090125000002, 1.2439538756291677, 1.2803661745542874},
{4.646584307291665, 6.921406786458336, 1.2122369919164142, 1.3125983142222468},
{4.637999999999997, 6.938666666666669, 1.1800048522484543, 1.3453914049441247},
{4.629748192708331, 6.955869046875002, 1.1472117615265762, 1.3669004091470747},
{4.621833041666665, 6.973013208333335, 1.1138053604803075, 1.3328203506075464},
{4.614258703124998, 6.990098432291669, 1.0797253019407789, 1.297996621544474},
{4.607029333333332, 7.007124000000003, 1.0449015728777058, 1.2623473872120385},
{4.600149088541666, 7.0240891927083355, 1.00925233854527, 1.2257761790897366},
{4.593622125, 7.040993291666669, 0.9726811304229672, 1.1881681636855994},
{4.587452598958333, 7.057835578125003, 0.9350731150188297, 1.1493850945966617},
{4.581644666666666, 7.074615333333336, 0.8962900459298926, 1.109258329033267},
{4.576202484374999, 7.091331838541668, 0.8561632803664979, 1.0675789133486013},
{4.571130208333333, 7.107984375000003, 0.8144838646818316, 1.0240830731365698},
{4.566431994791666, 7.124572223958335, 0.7709880244698004, 0.978430194961657},
{4.562111999999999, 7.141094666666669, 0.7253351462948879, 0.9301679142432349},
{4.558174380208333, 7.1575509843750025, 0.6770728655764653, 0.8786736585580837},
{4.554623291666665, 7.173940458333336, 0.6255786098913138, 0.8230497135776158},
{4.5514628906249985, 7.190262369791669, 0.5699546649108452, 0.7619166226084086},
{4.548697333333331, 7.206516000000002, 0.5088215739416384, 0.6929500767480814},
{4.546330776041666, 7.222700630208336, 0.4398550280813111, 0.6116144072372727},
{4.544367375, 7.238815541666669, 0.3585193585705028, 0.5061900973335405},
{4.542811286458333, 7.2548600156250025, 0.2530950486667708, 0.25309504866677024},
{4.541666666666666, 7.270833333333336, 0, 0},
};