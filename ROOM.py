
[
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Entrance Hallway
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Living Room
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Kitchen
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Bedroom
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Bathroom
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Library
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Secret Passage
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Garden
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Laboratory
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],  # Storage
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # Observatory
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],  # Game Room
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Dining Room
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Cinema
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Art Studio
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # Music Room
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Workshop
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # Wine Cellar
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Fitness Room
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Roof Terrace
]


adjacency_list = {
    "Entrance Hallway": [1],
    "Living Room": [0, 2, 5],
    "Kitchen": [1, 12],
    "Bedroom": [4, 8],
    "Bathroom": [3],
    "Library": [1, 6],
    "Storage": [5, 7, 8],
    "Garden": [6],
    "Laboratory": [3, 6],
    "Office": [13, 17],
    "Observatory": [16, 19],
    "Game Room": [14, 15, 18],
    "Dining Room": [2, 14],
    "Cinema": [9, 14],
    "Art Studio": [11, 12, 13],
    "Music Room": [11],
    "Workshop": [10, 17],
    "Wine Cellar": [9, 16],
    "Fitness Room": [11],
    "Roof Terrace": [10]
}

adjacency_list = {
    "Entrance Hallway": [(1,'W')],
    "Living Room": [(0,'E'), (2,'SE'), (5,'S')],
    "Kitchen": [(1,'NW'), (12,'S')],
    "Bedroom": [(4,'N'), (8,'S')],
    "Bathroom": [(3,'S')],
    "Library": [(1,'N'), (6,'Secret Passage on the South')],
    "Storage": [(5,'Secret Passage on the East'), (7,'N'), (8,'W')],
    "Garden": [(6,'S')],
    "Laboratory": [(3,'N'), (6,'E')],
    "Office": [(13,'Elevator Down'), (17,'E')],
    "Observatory": [(16,'W'), (19,'Upstaris')],
    "Game Room": [(14,'E'), (15,'W'), (18,'N')],
    "Dining Room": [(2,'N'), (14,'Downstairs')],
    "Cinema": [(9,'Elevator Up'), (14,'N')],
    "Art Studio": [(11,'W'), (12,'Upstairs'), (13,'S')],
    "Music Room": [(11,'E')],
    "Workshop": [(10,'N'), (17,'E')],
    "Wine Cellar": [(9,'E'), (16,'S')],
    "Fitness Room": [(11,'S')],
    "Roof Terrace": [(10,'Downstairs')]
}

connections = [connections for room, connections in adjacency_list.items()]
rooms = [(room) for room, connections in adjacency_list.items()]

adjacency_list_as_list = []
for room, connections in adjacency_list.items():
    adjacency_list_as_list.append([room, connections])
for i in adjacency_list_as_list:
    print(i)

[[(1, 'W')],
 [(0, 'E'), (2, 'SE'), (5, 'S')],
 [(1, 'NW'), (12, 'S')],
 [(4, 'N'), (8, 'S')],
 [(3, 'S')],
 [(1, 'N'),(6, 'Secret Passage on the South')],
 [(5, 'Secret Passage on the East'), (7, 'N'), (8, 'W')],
 [(6, 'S')],
 [(3, 'N'), (6, 'E')],
 [(13, 'Elevator Down'),(17, 'E')],
 [(16, 'W'), (19, 'Upstaris')],
 [(14, 'E'), (15, 'W'), (18, 'N')],
 [(2, 'N'), (14, 'Downstairs')],
 [(9, 'Elevator Up'), (14, 'N')],
 [(11, 'W'), (12, 'Upstairs'), (13, 'S')],
 [(11, 'E')],
 [(10, 'N'), (17, 'E')],
 [(9, 'E'), (16, 'S')],
 [(11, 'S')],
 [(10, 'Downstairs')]]

rooms_list = [
    ['Entrance Hallway', 'A grand entrance with polished marble floors and a dazzling crystal chandelier, setting the tone for your luxurious sleepover at your uncle\'s opulent mansion.', [], [(1, 'W')]],
    ['Living Room', 'Lavish with plush sofas, a roaring fireplace, and expansive windows overlooking the moonlit garden, providing a perfect setting for sophisticated late-night conversations.', [], [(0, 'E'), (2, 'SE'), (5, 'S')]],
    ['Kitchen', 'State-of-the-art appliances and a warm ambiance, filled with the enticing aroma of gourmet dishes prepared exclusively for your uncle\'s esteemed guests.', [], [(1, 'NW'), (12, 'S')]],
    ['Bedroom', 'The master bedroom, adorned with elegant furnishings, a king-sized bed, and luxurious linens, ensuring a night of unparalleled comfort during your lavish sleepover.', [('Golden Locket', 'A delicate locket containing a miniature portrait, radiating an air of opulence and familial history.')], [(4, 'N'), (8, 'S')]],
    ['Bathroom', 'A pristine space with a jacuzzi, a rainforest shower, and gold-accented fixtures, offering the epitome of indulgence for your pre-sleep relaxation.', [('Mysterious Key', 'An ornate key with intricate engravings, its purpose shrouded in mystery and luxury.')], [(3, 'S')]],
    ['Library', 'Rows of bookshelves showcasing leather-bound classics and rare first editions, providing a refined atmosphere for your late-night literary pursuits.', [('Broken Hand Mirror', 'A gilded hand mirror with delicately cracked glass, evoking a sense of past elegance and mystery.')], [(1, 'N'), (6, 'Secret Passage on the South')]],
    ['Storage', 'A concealed doorway behind a bookshelf, revealing a hidden corridor that adds an air of intrigue to your luxurious sleepover adventure.', [('Treasure Chest', 'A meticulously crafted chest with intricate carvings, promising hidden treasures that align with the luxurious theme of your sleepover.')], [(5, 'Secret Passage on the East'), (7, 'N'), (8, 'W')]],
    ['Garden', 'An impeccably landscaped outdoor space with fragrant flowers, a tranquil fountain, and meandering pathways, creating an enchanting backdrop for your opulent sleepover.', [], [(6, 'S')]],
    ['Laboratory', 'Equipped with cutting-edge scientific instruments and glassware, showcasing your uncle\'s dedication to luxury and innovation during your sleepover.', [], [(3, 'N'), (6, 'E')]],
    ['Office', 'A sleek, private office space with modern furnishings, offering a secluded retreat for business matters during your luxurious sleepover.', [], [(13, 'Elevator Down'), (17, 'E')]],
    ['Observatory', 'A domed room with a high-powered telescope, offering breathtaking views of the night sky, perfect for celestial observations during your sophisticated sleepover.', [('Celestial Globe', 'A luxurious celestial globe crafted from fine materials, showcasing the positions of stars and planets with an added touch of sophistication.')], [(16, 'W'), (19, 'Upstairs')]],
    ['Game Room', 'An entertainment haven with designer board games, vintage arcade machines, and a bespoke pool table, guaranteeing hours of refined amusement for your sleepover.', [('Chess Set', 'A handcrafted chess set with gold and silver pieces, inviting strategic contemplation in the lap of luxury during your sleepover.')], [(14, 'E'), (15, 'W'), (18, 'N')]],
    ['Dining Room', 'A formal setting with a grand dining table, adorned with fine china and crystal chandeliers, setting the stage for an exquisite midnight feast during your luxurious sleepover.', [('Ancient Scroll', 'A weathered parchment adorned with gold leaf, engraved with ancient symbols and hidden messages, adding an extra layer of luxury to your sleepover adventure.')], [(2, 'N'), (14, 'Downstairs')]],
    ['Cinema', 'A private home theater with plush seating, state-of-the-art audiovisual equipment, and a curated selection of films, promising an exclusive cinematic experience for your sleepover.', [], [(9, 'Elevator Up'), (14, 'N')]],
    ['Art Studio', 'Splattered with vibrant pigments, this artistic haven houses canvases, easels, and sculptures, providing a touch of cultural elegance to your sleepover.', [('Painter\'s Palette', 'A deluxe painter\'s palette adorned with gold leaf and premium pigments, emphasizing the artistic refinement of your uncle\'s possessions.')], [(11, 'W'), (12, 'Upstairs'), (13, 'S')]],
    ['Music Room', 'Impeccably designed with various instruments, sheet music, and acoustically perfect surroundings, inviting guests to indulge in a refined musical experience during your sleepover.', [('Musical Note Sheet', 'A sheet of musical notes written in elegant script, hinting at a musical masterpiece waiting to be discovered in the luxurious mansion during your sleepover.')], [(11, 'E')]],
    ['Workshop', 'A creatively charged space with premium tools, workbenches, and artistic projects in progress, reflecting the passion for luxury craftsmanship during your sleepover.', [], [(10, 'N'), (17, 'E')]],
    ['Wine Cellar', 'Rows of exquisite wine racks and barrels, creating a sophisticated ambiance for wine enthusiasts to explore and savor during your luxurious sleepover.', [], [(9, 'E'), (16, 'S')]],
    ['Fitness Room', 'Outfitted with high-end exercise machines, weights, and mirrored walls, allowing guests to maintain their wellness routines in luxury during the sleepover.', [('Baseball Bat', 'A polished wooden bat, more likely a decorative piece than a tool, reflecting the luxurious taste of your uncle\'s possessions.')], [(11, 'S')]],
    ['Roof Terrace', 'An expansive outdoor terrace with panoramic views, plush seating, and a private bar, providing an exclusive retreat for relaxation and stargazing during your opulent sleepover.', [], [(10, 'Downstairs')]]
]

connection_descriptions = [
    ('Entrance Hallway', 'Living Room', (1, 'W', 'an archway adorned with intricate carvings.')),
    ('Living Room', 'Entrance Hallway', (0, 'E', 'a grand doorway with a welcoming ambiance.')),
    ('Living Room', 'Kitchen', (2, 'SE', 'a swinging door leading to the kitchen.')),
    ('Living Room', 'Library', (6, 'Secret Passage on the South', 'a wide entrance to the library.')),
    ('Kitchen', 'Living Room', (1, 'NW', 'a swinging door connecting to the living room.')),
    ('Kitchen', 'Dining Room', (14, 'Downstairs', 'a formal entrance to the dining room.')),
    ('Bedroom', 'Bathroom', (3, 'S', 'a narrow passage leading to the en-suite bathroom.')),
    ('Bedroom', 'Laboratory', (6, 'E', 'a secure door to the laboratory.')),
    ('Bathroom', 'Bedroom', (4, 'N', 'a simple door connecting to the master bedroom.')),
    ('Library', 'Living Room', (1, 'N', 'a large wooden door leading to the living room.')),
    ('Library', 'Storage', (5, 'Secret Passage on the East', 'a concealed door leading to the storage room.')),
    ('Storage', 'Library', (5, 'Secret Passage on the East', 'a concealed door leading back to the library.')),
    ('Storage', 'Garden', (6, 'S', 'a hidden entrance to the garden.')),
    ('Storage', 'Laboratory', (6, 'E', 'a hidden entrance to the laboratory.')),
    ('Garden', 'Storage', (5, 'Secret Passage on the East', 'a rustic gate leading back to the storage room.')),
    ('Laboratory', 'Bedroom', (4, 'N', 'a secure door connecting to the bedroom.')),
    ('Laboratory', 'Storage', (5, 'Secret Passage on the East', 'a hidden entrance to the storage room.')),
    ('Office', 'Cinema', (9, 'Elevator Down', 'an entrance to the private cinema.')),
    ('Office', 'Wine Cellar', (16, 'S', 'a stairwell leading down to the wine cellar.')),
    ('Observatory', 'Workshop', (17, 'E', 'a high-tech door to the workshop.')),
    ('Observatory', 'Roof Terrace', (19, 'Upstairs', 'a spiral staircase to the roof terrace.')),
    ('Game Room', 'Music Room', (15, 'W', 'an open doorway connecting the game room to the music room.')),
    ('Game Room', 'Art Studio', (18, 'N', 'an entrance to the art studio.')),
    ('Game Room', 'Fitness Centre', (11, 'S', 'a glass door leading to the fitness center.')),
    ('Dining Room', 'Kitchen', (2, 'N', 'an entrance to the kitchen.')),
    ('Dining Room', 'Art Studio', (18, 'N', 'a staircase leading to the art studio.')),
    ('Cinema', 'Art Studio', (13, 'S', 'a door to the art studio.')),
    ('Cinema', 'Office', (17, 'E', 'an entrance to the office.')),
    ('Art Studio', 'Cinema', (13, 'S', 'an open doorway connecting the art studio to the cinema.')),
    ('Art Studio', 'Dining Room', (2, 'N', 'a staircase leading to the dining room.')),
    ('Art Studio', 'Game Room', (14, 'E', 'an entrance to the game room.')),
    ('Music Room', 'Game Room', (14, 'E', 'an open doorway connecting the music room to the game room.')),
    ('Workshop', 'Observatory', (16, 'S', 'an entrance to the observatory.')),
    ('Workshop', 'Wine Cellar', (9, 'Elevator Up', 'an entrance to the wine cellar.')),
    ('Wine Cellar', 'Workshop', (16, 'S', 'a wooden door leading back to the workshop.')),
    ('Wine Cellar', 'Office', (17, 'E', 'an entrance to the office.')),
    ('Fitness Room', 'Game Room', (14, 'E', 'a glass door connecting the fitness room to the game room.')),
    ('Roof Terrace', 'Observatory', (16, 'W', 'a staircase leading back to the observatory.'))
]

# Merge connection descriptions into the rooms_list
for room in rooms_list:
    room_name = room[0]
    room[3] = [connection[2] for connection in connection_descriptions if connection[0] == room_name]

for room in rooms_list:
    print(room)

rooms_list = [
    ['Entrance Hallway', "A grand entrance with polished marble floors and a dazzling crystal chandelier, setting the tone for your luxurious sleepover at your uncle's opulent mansion.", [], [(1, 'W', 'an archway adorned with intricate carvings.')]],
    ['Living Room', 'Lavish with plush sofas, a roaring fireplace, and expansive windows overlooking the moonlit garden, providing a perfect setting for sophisticated late-night conversations.', [], [(0, 'E', 'a grand doorway with a welcoming ambiance.'), (2, 'SE', 'a swinging door leading to the kitchen.'), (6, 'Secret Passage on the South', 'a wide entrance to the library.')]],
    ['Kitchen', "State-of-the-art appliances and a warm ambiance, filled with the enticing aroma of gourmet dishes prepared exclusively for your uncle's esteemed guests.", [], [(1, 'NW', 'a swinging door connecting to the living room.'), (14, 'Downstairs', 'a formal entrance to the dining room.')]],
    ['Bedroom', 'The master bedroom, adorned with elegant furnishings, a king-sized bed, and luxurious linens, ensuring a night of unparalleled comfort during your lavish sleepover.', [('Golden Locket', 'A delicate locket containing a miniature portrait, radiating an air of opulence and familial history.')], [(3, 'S', 'a narrow passage leading to the en-suite bathroom.'), (6, 'E', 'a secure door to the laboratory.')]],
    ['Bathroom', 'A pristine space with a jacuzzi, a rainforest shower, and gold-accented fixtures, offering the epitome of indulgence for your pre-sleep relaxation.', [('Mysterious Key', 'An ornate key with intricate engravings, its purpose shrouded in mystery and luxury.')], [(4, 'N', 'a simple door connecting to the master bedroom.')]],
    ['Library', 'Rows of bookshelves showcasing leather-bound classics and rare first editions, providing a refined atmosphere for your late-night literary pursuits.', [('Broken Hand Mirror', 'A gilded hand mirror with delicately cracked glass, evoking a sense of past elegance and mystery.')], [(1, 'N', 'a large wooden door leading to the living room.'), (5, 'Secret Passage on the East', 'a concealed door leading to the storage room.')]],
    ['Storage', 'A dimly lit storage room with dusty crates and forgotten relics, creating an air of mystery and intrigue. The scent of aged wood and faint whispers of the past linger, adding an unexpected layer to your opulent sleepover adventure', [('Treasure Chest', 'A meticulously crafted chest with intricate carvings, promising hidden treasures that align with the luxurious theme of your sleepover.')], [(5, 'Secret Passage on the East', 'a concealed door leading back to the library.'), (6, 'S', 'a hidden entrance to the garden.'), (6, 'E', 'a hidden entrance to the laboratory.')]],
    ['Garden', 'An impeccably landscaped outdoor space with fragrant flowers, a tranquil fountain, and meandering pathways, creating an enchanting backdrop for your opulent sleepover.', [], [(5, 'Secret Passage on the East', 'a rustic gate leading back to the storage room.')]],
    ['Laboratory', "Equipped with cutting-edge scientific instruments and glassware, showcasing your uncle's dedication to luxury and innovation during your sleepover.", [], [(4, 'N', 'a secure door connecting to the bedroom.'), (5, 'Secret Passage on the East', 'a hidden entrance to the storage room.')]],
    ['Office', 'A sleek, private office space with modern furnishings, offering a secluded retreat for business matters during your luxurious sleepover.', [], [(9, 'Elevator Down', 'an entrance to the private cinema.'), (16, 'S', 'a stairwell leading down to the wine cellar.')]],
    ['Observatory', 'A domed room with a high-powered telescope, offering breathtaking views of the night sky, perfect for celestial observations during your sophisticated sleepover.', [('Celestial Globe', 'A luxurious celestial globe crafted from fine materials, showcasing the positions of stars and planets with an added touch of sophistication.')], [(17, 'E', 'a high-tech door to the workshop.'), (19, 'Upstairs', 'a spiral staircase to the roof terrace.')]],
    ['Game Room', 'An entertainment haven with designer board games, vintage arcade machines, and a bespoke pool table, guaranteeing hours of refined amusement for your sleepover.', [('Chess Set', 'A handcrafted chess set with gold and silver pieces, inviting strategic contemplation in the lap of luxury during your sleepover.')], [(15, 'W', 'an open doorway connecting the game room to the music room.'), (18, 'N', 'an entrance to the art studio.'), (11, 'S', 'a glass door leading to the fitness center.')]],
    ['Dining Room', 'A formal setting with a grand dining table, adorned with fine china and crystal chandeliers, setting the stage for an exquisite midnight feast during your luxurious sleepover.', [('Ancient Scroll', 'A weathered parchment adorned with gold leaf, engraved with ancient symbols and hidden messages, adding an extra layer of luxury to your sleepover adventure.')], [(2, 'N', 'an entrance to the kitchen.'), (18, 'N', 'a staircase leading to the art studio.')]],
    ['Cinema', 'A private home theater with plush seating, state-of-the-art audiovisual equipment, and a curated selection of films, promising an exclusive cinematic experience for your sleepover.', [], [(13, 'S', 'a door to the art studio.'), (17, 'E', 'an entrance to the office.')]],
    ['Art Studio', 'Splattered with vibrant pigments, this artistic haven houses canvases, easels, and sculptures, providing a touch of cultural elegance to your sleepover.', [("Painter's Palette", "A deluxe painter's palette adorned with gold leaf and premium pigments, emphasizing the artistic refinement of your uncle's possessions.")], [(13, 'S', 'an open doorway connecting the art studio to the cinema.'), (2, 'N', 'a staircase leading to the dining room.'), (14, 'E', 'an entrance to the game room.')]],
    ['Music Room', 'Impeccably designed with various instruments, sheet music, and acoustically perfect surroundings, inviting guests to indulge in a refined musical experience during your sleepover.', [('Musical Note Sheet', 'A sheet of musical notes written in elegant script, hinting at a musical masterpiece waiting to be discovered in the luxurious mansion during your sleepover.')], [(14, 'E', 'an open doorway connecting the music room to the game room.')]],
    ['Workshop', 'A creatively charged space with premium tools, workbenches, and artistic projects in progress, reflecting the passion for luxury craftsmanship during your sleepover.', [], [(16, 'S', 'an entrance to the observatory.'), (9, 'Elevator Up', 'an entrance to the wine cellar.')]],
    ['Wine Cellar', 'Rows of exquisite wine racks and barrels, creating a sophisticated ambiance for wine enthusiasts to explore and savor during your luxurious sleepover.', [], [(16, 'S', 'a wooden door leading back to the workshop.'), (17, 'E', 'an entrance to the office.')]],
    ['Fitness Room', 'Outfitted with high-end exercise machines, weights, and mirrored walls, allowing guests to maintain their wellness routines in luxury during the sleepover.', [('Baseball Bat', "A polished wooden bat, more likely a decorative piece than a tool, reflecting the luxurious taste of your uncle's possessions.")], [(14, 'E', 'a glass door connecting the fitness room to the game room.')]],
    ['Roof Terrace', 'An expansive outdoor terrace with panoramic views, plush seating, and a private bar, providing an exclusive retreat for relaxation and stargazing during your opulent sleepover.', [], [(16, 'W', 'a staircase leading back to the observatory.')]]
]