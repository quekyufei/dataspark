from flask import Flask, render_template, request
import jsgmapspackage.generate_html as map_helper

app = Flask(__name__)




@app.route('/form/')
def form():
	coordinates=[
		{'123':'[{lat: 1.37060695394614, lng: 103.89266808874676}, {lat: 1.368308353364, lng: 103.89393838248249}, {lat: 1.36637999879956, lng: 103.89194715850095}, {lat: 1.36395805601148, lng: 103.89261277802149}, {lat: 1.3597807263938, lng: 103.89332464938751}, {lat: 1.3568307844677, lng: 103.89260949897677}, {lat: 1.35385498086943, lng: 103.89147049226345}, {lat: 1.35110728949265, lng: 103.8903098431232}, {lat: 1.34780294127385, lng: 103.89030740867446}, {lat: 1.34503285502097, lng: 103.89113604973045}, {lat: 1.34151105876514, lng: 103.89189250385124}, {lat: 1.33901443022109, lng: 103.89506854137488}, {lat: 1.33638181561906, lng: 103.89785574766542}, {lat: 1.33375855817569, lng: 103.9005998503616}, {lat: 1.33073374785934, lng: 103.90373154551283}, {lat: 1.32884628389091, lng: 103.90546507501655}, {lat: 1.32306974700238, lng: 103.90560762847845}, {lat: 1.32135678897249, lng: 103.90537221650075}, {lat: 1.31709537499354, lng: 103.90295147896967}, {lat: 1.31634170548514, lng: 103.89891621295058}, {lat: 1.31569833821527, lng: 103.89559528546464}, {lat: 1.3151892235607, lng: 103.89331774481381}, {lat: 1.314713072947, lng: 103.89084333204679}, {lat: 1.31402602433639, lng: 103.88729074830816}, {lat: 1.31359869606059, lng: 103.88497531416832}, {lat: 1.31274483593155, lng: 103.88080516731976}, {lat: 1.31214703288286, lng: 103.87715016317217}, {lat: 1.31077707819718, lng: 103.87363663982293}, {lat: 1.30992336177794, lng: 103.87144344651483}, {lat: 1.3094187398083, lng: 103.86753497349068}, {lat: 1.30774601733202, lng: 103.8642627465441}, {lat: 1.30495670239172, lng: 103.86363028484124}, {lat: 1.30337552638813, lng: 103.85963089198265}, {lat: 1.30033057855542, lng: 103.85716080665901}, {lat: 1.29820784139683, lng: 103.85549139837407}, {lat: 1.2966729849642, lng: 103.85441422464267}, {lat: 1.29208221483052, lng: 103.85125994680256}, {lat: 1.29043039362749, lng: 103.85026216508201}, {lat: 1.28724656561704, lng: 103.84833343750249}, {lat: 1.28398513155185, lng: 103.84527387289731}, {lat: 1.2860773006121, lng: 103.84244788580838}]'},
		{'234':'[{lat: 1.37060695394614, lng: 103.89266808874676}, {lat: 1.37016500002901, lng: 103.89535999996711}, {lat: 1.37239666924933, lng: 103.89777362456783}, {lat: 1.37514056376267, lng: 103.89724811886428}, {lat: 1.37668753222312, lng: 103.89393761218089}, {lat: 1.37634448413795, lng: 103.89149353867691}, {lat: 1.37528677811119, lng: 103.88918760776436}, {lat: 1.37291834719604, lng: 103.88673982857989}, {lat: 1.37079666702428, lng: 103.88521000000019}, {lat: 1.37063835467565, lng: 103.882445169636}, {lat: 1.37022333300436, lng: 103.8802849999831}, {lat: 1.36921737828483, lng: 103.87814733411857}, {lat: 1.36856637012739, lng: 103.8762710483349}, {lat: 1.36605804817414, lng: 103.87522122785421}, {lat: 1.36327972197547, lng: 103.87383805598819}, {lat: 1.36133997852966, lng: 103.87363460960414}, {lat: 1.35999305129204, lng: 103.87393532776181}, {lat: 1.35663166702793, lng: 103.87410388898788}, {lat: 1.35339155862192, lng: 103.87285801649963}, {lat: 1.3490461240579, lng: 103.87341165935781}, {lat: 1.34698958928417, lng: 103.87205488524701}, {lat: 1.34483265931476, lng: 103.8710922003054}, {lat: 1.34196277802503, lng: 103.8709686110327}, {lat: 1.33845332842129, lng: 103.87084881783568}, {lat: 1.33596832935372, lng: 103.87051588342655}, {lat: 1.33320166700854, lng: 103.86976166703383}, {lat: 1.33099030126892, lng: 103.86922890950602}, {lat: 1.32986133945973, lng: 103.86896099565628}, {lat: 1.32634025655419, lng: 103.86834025123765}, {lat: 1.32409476572475, lng: 103.86764196002876}, {lat: 1.32204861560134, lng: 103.86628982237994}, {lat: 1.31889711409084, lng: 103.8642148620878}, {lat: 1.31456420794151, lng: 103.86086821464755}, {lat: 1.31284472583438, lng: 103.85989088288474}, {lat: 1.31038833299803, lng:103.85870666696984}, {lat: 1.30653024120879, lng: 103.8561630249311}, {lat: 1.30431906266143, lng: 103.85501564257024}, {lat: 1.30097493989394, lng: 103.8521798624137}, {lat: 1.29807216909408, lng: 103.84975607305783}, {lat: 1.29489484954945, lng: 103.85108138663934}, {lat: 1.29276132399953, lng: 103.84983741344308}, {lat: 1.29044830830726, lng: 103.84875123545265}, {lat: 1.28882717929599, lng: 103.8474938118651}, {lat: 1.28676420118491, lng: 103.84575036447065}, {lat: 1.28531114761754, lng: 103.84455070696784}, {lat: 1.28293819129834, lng: 103.84254276754574}, {lat: 1.28118388885484, lng: 103.84105000000471}, {lat: 1.28027629959632, lng: 103.84029791443083}, {lat: 1.2777380589964, lng: 103.83749709165197}, {lat: 1.27605834770353, lng: 103.83519065305671}, {lat: 1.2774116353284, lng: 103.83214410914843}, {lat: 1.27860472196885, lng: 103.82948638898173}, {lat: 1.28045309423663, lng: 103.82638920754815}, {lat: 1.28105845355429, lng: 103.82528065411316}, {lat: 1.2822783541702, lng: 103.82241744338572}, {lat: 1.28394108576437, lng: 103.81783962251122}, {lat: 1.28502568134889, lng: 103.81374366011399}, {lat: 1.28592835098556, lng: 103.80935410958449}, {lat: 1.28619141382394, lng: 103.80686549059318}, {lat: 1.28941805603102, lng: 103.80228694398484}, {lat: 1.29119666696879, lng: 103.80045500000118}, {lat: 1.29624499998226, lng: 103.79952333299494}, {lat: 1.29872166703909, lng: 103.8002979755481}, {lat: 1.30213305598263, lng: 103.79839083302141}, {lat: 1.30535666699303, lng: 103.79479722196947}, {lat: 1.30722333300814, lng: 103.79227638896938}, {lat: 1.30801640815091, lng: 103.7883731546267}, {lat: 1.30781638901709, lng: 103.78423666696615}, {lat: 1.30965490194051, lng: 103.7812018067838}, {lat: 1.31123416666912, lng: 103.77838361113201}, {lat: 1.31235972197855, lng: 103.77552750001337}, {lat: 1.31169519353522, lng: 103.76960993525367}, {lat: 1.31240993603605, lng: 103.76685476875124}, {lat: 1.31497399268611, lng: 103.76502698264449}, {lat: 1.31491572870629, lng: 103.76412225438476}, {lat: 1.31491572870629, lng: 103.76412225438476}, {lat: 1.312440556, lng: 103.7658489}, {lat: 1.311975556, lng: 103.7698144}, {lat: 1.31266302174215, lng: 103.77479215922537}, {lat: 1.31167951129602, lng: 103.77868390552867}, {lat: 1.3095609201372, lng: 103.78201879388226}, {lat: 1.30807305598128, lng: 103.78475916699466}, {lat: 1.30837970735444, lng: 103.78843145303215}, {lat: 1.30740138898924, lng: 103.79254222202354}, {lat: 1.30627521395682, lng: 103.79427940117534}, {lat: 1.30270500001823, lng: 103.79838166697326}, {lat: 1.29882892782979, lng: 103.80097389222824}, {lat: 1.2954609366563, lng: 103.79952549937242}, {lat: 1.29245762862665, lng: 103.79998683928974}, {lat: 1.29013472201419, lng: 103.80202111098815}, {lat: 1.28679632523156, lng: 103.80565677295323}, {lat: 1.28635135443034, lng: 103.8081000223439}, {lat: 1.28598009010704, lng: 103.81122515087834}, {lat: 1.28531403163162, lng: 103.81365537642607}, {lat: 1.28420923932422, lng: 103.81765723225827}, {lat: 1.28292332245689, lng: 103.82165660905856}, {lat: 1.2803950142786, lng: 103.82708906887606}, {lat: 1.27855472196877, lng: 103.83008250001669}, {lat: 1.27739664167497, lng: 103.83275178077875}, {lat: 1.27623302424393, lng: 103.83483786772155}, {lat: 1.27832046633393, lng: 103.83762574759974}, {lat: 1.27900819665099, lng: 103.83860360621959}, {lat: 1.28154583300728, lng: 103.84087722199499}, {lat: 1.28571089865595, lng: 103.84437203405348}]'},
		{'345':'[{lat: 1.28635135443034, lng: 103.8081000223439}, {lat: 1.28598009010704, lng: 103.81122515087834}, {lat: 1.28531403163162, lng: 103.81365537642607}, {lat: 1.28420923932422, lng: 103.81765723225827}, {lat: 1.28292332245689, lng: 103.82165660905856}, {lat: 1.2803950142786, lng: 103.82708906887606}, {lat: 1.27855472196877, lng: 103.83008250001669}, {lat: 1.27739664167497, lng: 103.83275178077875}, {lat: 1.27623302424393, lng: 103.83483786772155}, {lat: 1.27832046633393, lng: 103.83762574759974}, {lat: 1.27900819665099, lng: 103.83860360621959}, {lat: 1.28154583300728, lng: 103.84087722199499}, {lat: 1.28571089865595, lng: 103.84437203405348}, {lat: 1.28898962180798, lng: 103.84708976365569}, {lat: 1.29084476137495, lng: 103.84857901022669}, {lat: 1.29411640848293, lng: 103.85020606905503}, {lat: 1.29618544092334, lng: 103.84958029974611}, {lat: 1.29921444445586, lng: 103.84910329217985}, {lat: 1.30099699058522, lng: 103.8498101874305}, {lat: 1.30324521574524, lng: 103.84995776766847}, {lat: 1.30572083298412, lng: 103.85120583303191}, {lat: 1.30879366465919, lng: 103.8531751994068}, {lat: 1.31313747728456, lng: 103.8563561439714}, {lat: 1.31503278656775, lng: 103.85788270432104}, {lat: 1.31783421341306, lng: 103.86004042483177}, {lat: 1.32008815616383, lng: 103.86179781146463}, {lat: 1.32258753768004, lng: 103.86385682733587}, {lat: 1.32477289725503, lng: 103.8655673081052}]'},
		{'456':'[{lat: 1.36133997852966, lng: 103.87363460960414}, {lat: 1.35999305129204, lng: 103.87393532776181}, {lat: 1.35663166702793, lng: 103.87410388898788}, {lat: 1.35339155862192, lng: 103.87285801649963}, {lat: 1.3490461240579, lng: 103.87341165935781}, {lat: 1.34698958928417, lng: 103.87205488524701}, {lat: 1.34483265931476, lng: 103.8710922003054}, {lat: 1.34196277802503, lng: 103.8709686110327}, {lat: 1.33845332842129, lng: 103.87084881783568}, {lat: 1.33596832935372, lng: 103.87051588342655}, {lat: 1.33320166700854, lng: 103.86976166703383}, {lat: 1.33099030126892, lng: 103.86922890950602}, {lat: 1.32986133945973, lng: 103.86896099565628}, {lat: 1.32634025655419, lng: 103.86834025123765}, {lat: 1.32409476572475, lng: 103.86764196002876}, {lat: 1.32204861560134, lng: 103.86628982237994}, {lat: 1.31889711409084, lng: 103.8642148620878}, {lat: 1.31456420794151, lng: 103.86086821464755}, {lat: 1.31284472583438, lng: 103.85989088288474}, {lat: 1.31038833299803, lng: 103.85870666696984}, {lat: 1.30653024120879, lng: 103.8561630249311}, {lat: 1.30431906266143, lng: 103.85501564257024}]'},
		{'567':'[{lat: 1.3568307844677, lng: 103.89260949897677}, {lat: 1.35385498086943, lng: 103.89147049226345}, {lat: 1.35110728949265, lng: 103.8903098431232}, {lat: 1.32991690265608, lng: 103.86027368842302}]'}
	]
	map_helper.generate_html(coordinates)
	return render_template('results.html')
	#return render_template('form.html')

@app.route('/',methods=['POST','GET'])
def process_form():
	if request.method == 'POST':
		#request.form is a dictionary with the values from the form

		#send request.form to chiilek, chiilek returns top 5 OD pair + footfall
		top_od_pairs = chiilek_function(request.form)
		#send request.form to danseb; danseb returns top 5 footfall locations
		top_locations = danseb_function(request.form)

		#pass each OD pair to danseb, recieve the route coordinates for each pair
		coordinates = []
		for od_pair in top_od_pairs:
			coordinates.append(danseb_routes_function(od_pair[0], od_pair[1]))
		
		#plot route.
		map_helper.generate_html(top_locations, coordinates)
		return render_template('results.html')

	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)