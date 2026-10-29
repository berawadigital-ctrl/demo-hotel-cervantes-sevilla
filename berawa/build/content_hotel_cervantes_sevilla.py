# Contenido de la demo Hotel Cervantes (Sevilla) (es/ca/en/fr). Hechos de hotel-cervantes.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble de uso individual','Habitación doble','Doble con sofá-cama'],
'ca':['Doble d\'ús individual','Habitació doble','Doble amb sofà llit'],
'en':['Double for single use','Double room','Double with sofa bed'],
'fr':['Double à usage individuel','Chambre double','Double avec canapé-lit']}
RD={
'es':['Con suelos de madera y diseño funcional y elegante, ideal para 1 persona: cama de 1,35 m, baño privado, climatizada e insonorizada.','Habitación de unos 15 m2, con suelos de madera, para 2 personas: una cama doble o dos camas individuales, baño privado, climatización e insonorización.','Espaciosa habitación para 3 personas, con 1 cama doble más 1 sofá-cama, baño privado y climatización.'],
'ca':['Amb terra de fusta i disseny funcional i elegant, ideal per a 1 persona: llit d\'1,35 m, bany privat, climatitzada i insonoritzada.','Habitació d\'uns 15 m2, amb terra de fusta, per a 2 persones: un llit doble o dos llits individuals, bany privat, climatització i insonorització.','Espaiosa habitació per a 3 persones, amb 1 llit doble més 1 sofà llit, bany privat i climatització.'],
'en':['With wooden floors and a functional, elegant design, ideal for 1 guest: a 1.35 m bed, private bathroom, air-conditioned and soundproofed.','A room of about 15 m2, with wooden floors, for 2 guests: one double bed or two single beds, private bathroom, climate control and soundproofing.','Spacious room for 3 guests, with 1 double bed plus 1 sofa bed, private bathroom and climate control.'],
'fr':['Avec parquet et un design fonctionnel et élégant, idéale pour 1 personne : lit de 1,35 m, salle de bain privée, climatisée et insonorisée.','Chambre d\'environ 15 m2, avec parquet, pour 2 personnes : un lit double ou deux lits simples, salle de bain privée, climatisation et insonorisation.','Chambre spacieuse pour 3 personnes, avec 1 lit double plus 1 canapé-lit, salle de bain privée et climatisation.']}
ART={
'hero':('arches',9401,['#f1dfc2','#f8ecd2','#e0a35c','#c98a5e','#a8553a']),
'intro':('columns',9402,['#efe0c4','#f7ecd4','#d99a52','#c68c64','#9a4a38']),
'r1':('arches',9411,['#f0dfc4','#f8ebd1','#dd9f58','#c8905f','#a05040']),
'r2':('columns',9412,['#ecdcc2','#f6e9d0','#d79852','#c58a60','#97493a']),
'r3':('skyline',9413,['#4b3a52','#ee9c6c','#ffdfa6','#4c3b55','#3a2c46','#271d34']),
'g1':('skyline',9421,['#3a3f68','#ee9a68','#fddca2','#3a4066','#2c3254','#1c2240']),
'g2':('arches',9422,['#f2e1c6','#f9edd4','#e1a45e','#cb9060','#a45342']),
'g3':('columns',9423,['#eddfc5','#f6ead1','#d89b55','#c68d63','#9a4c3c']),
'g4':('hills',9424,['#e6e4d0','#f6e8c6','#ffe2a8','#b9c6a3','#8da785','#5f8062']),
'g5':('waves',9425,['#f5ddae','#eb9c76','#fff0c0','#79afc4','#4c8ea9','#2f6c87','#1c4a63']),
'g6':('skyline',9426,['#2e3a5e','#e68a62','#fbd09a','#2d3a5b','#212f4a','#151f31'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Cervantes · Hotel de cuatro estrellas en el centro de Sevilla',see_rooms='Ver habitaciones',hero_k='Sevilla · La Campana',hero_t='Un hotel con encanto en el centro histórico de Sevilla',hero_s='Edificio del siglo XIX con patio sevillano, junto a la calle Sierpes, y recepción 24 horas.',
 intro_t='En el corazón de Sevilla',intro_p1='Hotel Cervantes está en la calle Cervantes 10-12, en la zona de La Campana, junto a la calle Sierpes, la plaza de la Encarnación y la Alameda de Hércules. Ocupa un edificio del siglo XIX reformado en 2003.',
 intro_p2='Tiene habitaciones dobles, de uso individual y con sofá-cama, desayuno buffet cada mañana, cafetería, garaje privado de pago y recepción 24 horas en español, francés, inglés e italiano.',
 stats=['4 estrellas','Calle Sierpes','Recepción 24 h','Patio sevillano'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Dobles, de uso individual y con sofá-cama.',
 svcs=['Wifi gratuito','Recepción 24 horas','Desayuno buffet','Cafetería','Garaje privado (de pago)','Alquiler de bicicletas','Servicio de lavandería y planchado','Congresos y catering'],
 loc_p='Calle Cervantes 10-12, 41003 Sevilla, en el centro histórico, en la zona de La Campana.',
 chips=['¿Qué tipos de habitación hay?','¿Hay parking?','¿Admiten mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Cervantes · Hotel de quatre estrelles al centre de Sevilla',see_rooms='Veure habitacions',hero_k='Sevilla · La Campana',hero_t='Un hotel amb encant al centre històric de Sevilla',hero_s='Edifici del segle XIX amb pati sevillà, al costat del carrer Sierpes, i recepció 24 hores.',
 intro_t='Al cor de Sevilla',intro_p1='Hotel Cervantes és al carrer Cervantes 10-12, a la zona de La Campana, al costat del carrer Sierpes, la plaça de la Encarnación i l\'Alameda de Hércules. Ocupa un edifici del segle XIX reformat el 2003.',
 intro_p2='Té habitacions dobles, d\'ús individual i amb sofà llit, esmorzar buffet cada matí, cafeteria, garatge privat de pagament i recepció 24 hores en castellà, francès, anglès i italià.',
 stats=['4 estrelles','Carrer Sierpes','Recepció 24 h','Pati sevillà'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Dobles, d\'ús individual i amb sofà llit.',
 svcs=['Wifi gratuït','Recepció 24 hores','Esmorzar buffet','Cafeteria','Garatge privat (de pagament)','Lloguer de bicicletes','Servei de bugaderia i planxa','Congressos i càtering'],
 loc_p='Carrer Cervantes 10-12, 41003 Sevilla, al centre històric, a la zona de La Campana.',
 chips=['Quins tipus d\'habitació hi ha?','Hi ha pàrquing?','Admeteu mascotes?','Com es reserva?']),
'en':dict(title='Hotel Cervantes · Four-star hotel in central Sevilla',see_rooms='See the rooms',hero_k='Sevilla · La Campana',hero_t='A charming hotel in the historic centre of Sevilla',hero_s='A nineteenth-century building with a Sevillian courtyard, next to Calle Sierpes, and 24-hour reception.',
 intro_t='In the heart of Sevilla',intro_p1='Hotel Cervantes is at Calle Cervantes 10-12, in the La Campana area, next to Calle Sierpes, Plaza de la Encarnación and Alameda de Hércules. It occupies a nineteenth-century building refurbished in 2003.',
 intro_p2='It has double rooms, doubles for single use and rooms with a sofa bed, a buffet breakfast every morning, a cafe, paid private garage and a 24-hour reception speaking Spanish, French, English and Italian.',
 stats=['4 stars','Calle Sierpes','24-hour reception','Sevillian courtyard'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Doubles, single use and with sofa bed.',
 svcs=['Free wifi','24-hour reception','Buffet breakfast','Cafe','Private garage (paid)','Bicycle rental','Laundry and ironing service','Conferences and catering'],
 loc_p='Calle Cervantes 10-12, 41003 Sevilla, in the historic centre, in the La Campana area.',
 chips=['What room types are there?','Is there parking?','Are pets allowed?','How do I book?']),
'fr':dict(title='Hotel Cervantes · Hôtel quatre étoiles au centre de Séville',see_rooms='Voir les chambres',hero_k='Séville · La Campana',hero_t='Un hôtel de charme dans le centre historique de Séville',hero_s='Un immeuble du XIXe siècle avec patio sévillan, près de la calle Sierpes, et réception 24 h/24.',
 intro_t='Au cœur de Séville',intro_p1='L\'Hotel Cervantes se trouve calle Cervantes 10-12, dans le quartier de La Campana, près de la calle Sierpes, de la plaza de la Encarnación et de l\'Alameda de Hércules. Il occupe un immeuble du XIXe siècle rénové en 2003.',
 intro_p2='Il propose des chambres doubles, doubles à usage individuel et avec canapé-lit, un petit-déjeuner buffet chaque matin, un café, un garage privé payant et une réception 24 h/24 en espagnol, français, anglais et italien.',
 stats=['4 étoiles','Calle Sierpes','Réception 24 h','Patio sévillan'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Doubles, usage individuel et avec canapé-lit.',
 svcs=['Wifi gratuit','Réception 24 h/24','Petit-déjeuner buffet','Café','Garage privé (payant)','Location de vélos','Service de blanchisserie et repassage','Congrès et traiteur'],
 loc_p='Calle Cervantes 10-12, 41003 Séville, dans le centre historique, quartier de La Campana.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il un parking ?','Les animaux sont-ils admis ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hotel-cervantes.com')
D=dict(name='Hotel Cervantes',ac='#8a3a2e',ac2='#c9923c',ac2_a11y='#6b4d12',book=BOOK,around=[],foot=FOOT,
 address='Calle Cervantes 10-12 · 41003 Sevilla',phones=['954 900 280'],emails=['info@hotel-cervantes.com'],maps='Hotel Cervantes, Calle Cervantes 10, Sevilla',t=T)
META=dict(repo='demo-hotel-cervantes-sevilla',name='Hotel Cervantes',legal_name='HOTEL RESIDENCIA CERVANTES, S.L.',registry_ids=['CIF B41242777','Registro Mercantil de Madrid, folio 39, tomo 13.165, hoja M-213.077'],
 url='https://www.hotel-cervantes.com/',domain='hotel-cervantes.com',municipality='Sevilla',province='Sevilla',sector='hotel de cuatro estrellas en el centro historico',
 read_at='2026-10-29T02:40:00+01:00',created_at='2026-10-29T02:39:00+01:00',built_at='2026-10-29T02:43:00+01:00',audit_date='@CREATED@',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T02:29:47+01:00',url='https://www.google.com/maps/place/Hotel+Cervantes+Sevilla/@37.3955646,-5.9932901,17z/data=!3m1!5s0xd126c05f23239c9:0x1667aa31d7f4cd2b!4m9!3m8!1s0xd126c05f480418f:0xbe84ae26f3268b73!5m2!4m1!1i2!8m2!3d37.3955646!4d-5.9932901!16s%2Fg%2F1tj2pqmv'),
 book=dict(mode='mail',email='info@hotel-cervantes.com',note='La web del negocio reserva con un motor externo; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel urbano de cuatro estrellas (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación hay?','K01'),('¿Hay wifi y caja fuerte?','K02'),('¿A qué hora es el check-in?','K03'),('¿Admiten mascotas?','K04'),('¿Hay parking?','K05'),('¿Hay desayuno?','K06'),('¿Cómo llego desde el aeropuerto?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Hay recepción 24 horas?','K11'),('¿Cuándo se construyó el edificio?','K12'),('¿Cuánto cuesta una habitación?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Hay piscina?',None),('¿Hay gimnasio?',None)],
'ca':[('Quins tipus d\'habitació hi ha?','K01'),('Hi ha wifi i caixa forta?','K02'),('A quina hora és el check-in?','K03'),('Admeteu mascotes?','K04'),('Hi ha pàrquing?','K05'),('Hi ha esmorzar?','K06'),('Com arribo des de l\'aeroport?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Hi ha recepció 24 hores?','K11'),('Quan es va construir l\'edifici?','K12'),('Quant costa una habitació?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Hi ha piscina?',None),('Hi ha gimnàs?',None)],
'en':[('What room types are there?','K01'),('Is there wifi and a safe?','K02'),('What time is check-in?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('Is there breakfast?','K06'),('How do I get there from the airport?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('Is there a 24-hour reception?','K11'),('When was the building constructed?','K12'),('How much is a room?',None),('Confirm that there is a free room tomorrow','K08'),('Is there a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quels types de chambre y a-t-il ?','K01'),('Y a-t-il le wifi et un coffre-fort ?','K02'),('À quelle heure est le check-in ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il un petit-déjeuner ?','K06'),('Comment venir depuis l\'aéroport ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Y a-t-il une réception 24 h/24 ?','K11'),('Quand l\'immeuble a-t-il été construit ?','K12'),('Combien coûte une chambre ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Y a-t-il une piscine ?',None),('Y a-t-il une salle de sport ?',None)]}
