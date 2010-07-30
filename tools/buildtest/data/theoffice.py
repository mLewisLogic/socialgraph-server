"""
Data representing relational data for "The Office"
Must include the following dictionaries:
    name
    users
    connections
"""

name = 'The Office'

users = [
    {'name':'Michael Scott'},
    {'name':'Jim Halpert'},
    {'name':'Dwight Schrute'},
    {'name':'Pam Beesly'},
    {'name':'Andy Bernard'},
    {'name':'Stanley Hudson'},
    {'name':'Phillis Lapin-Vance'},
    {'name':'Angela Martin'},
    {'name':'Kevin Malone'},
    {'name':'Oscar Martinez'},
    {'name':'Meredith Palmer'},
    {'name':'Kelly Kapoor'},
    {'name':'Creed Bratton'},
    {'name':'Ryan Howard'},
]

familiarity_connections = [
    {'user1':'Michael Scott', 'user2':'Jim Halpert', 'weight':0.7},
    {'user1':'Michael Scott', 'user2':'Dwight Schrute', 'weight':0.8},
    {'user1':'Michael Scott', 'user2':'Pam Beesly', 'weight':0.4},
    {'user1':'Michael Scott', 'user2':'Andy Bernard', 'weight':0.3},
    {'user1':'Michael Scott', 'user2':'Stanley Hudson', 'weight':0.2},
    {'user1':'Michael Scott', 'user2':'Phillis Lapin-Vance', 'weight':0.1},
    {'user1':'Michael Scott', 'user2':'Angela Martin', 'weight':0.3},
    {'user1':'Michael Scott', 'user2':'Kevin Malone', 'weight':0.3},
    {'user1':'Michael Scott', 'user2':'Oscar Martinez', 'weight':0.2},
    {'user1':'Michael Scott', 'user2':'Meredith Palmer', 'weight':0.1},
    {'user1':'Michael Scott', 'user2':'Kelly Kapoor', 'weight':0.1},
    {'user1':'Michael Scott', 'user2':'Creed Bratton', 'weight':0.2},
    {'user1':'Michael Scott', 'user2':'Ryan Howard', 'weight':0.4},
    
    {'user1':'Jim Halpert', 'user2':'Dwight Schrute', 'weight':0.8},
    {'user1':'Jim Halpert', 'user2':'Pam Beesly', 'weight':1.0},
    {'user1':'Jim Halpert', 'user2':'Andy Bernard', 'weight':0.6},
    {'user1':'Jim Halpert', 'user2':'Stanley Hudson', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Phillis Lapin-Vance', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Angela Martin', 'weight':0.2},
    {'user1':'Jim Halpert', 'user2':'Kevin Malone', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Oscar Martinez', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Jim Halpert', 'user2':'Kelly Kapoor', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Jim Halpert', 'user2':'Ryan Howard', 'weight':0.7},
    
    {'user1':'Dwight Schrute', 'user2':'Pam Beesly', 'weight':0.4},
    {'user1':'Dwight Schrute', 'user2':'Andy Bernard', 'weight':0.5},
    {'user1':'Dwight Schrute', 'user2':'Stanley Hudson', 'weight':0.3},
    {'user1':'Dwight Schrute', 'user2':'Phillis Lapin-Vance', 'weight':0.3},
    {'user1':'Dwight Schrute', 'user2':'Angela Martin', 'weight':0.9},
    {'user1':'Dwight Schrute', 'user2':'Kevin Malone', 'weight':0.4},
    {'user1':'Dwight Schrute', 'user2':'Oscar Martinez', 'weight':0.2},
    {'user1':'Dwight Schrute', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Dwight Schrute', 'user2':'Kelly Kapoor', 'weight':0.1},
    {'user1':'Dwight Schrute', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Dwight Schrute', 'user2':'Ryan Howard', 'weight':0.4},
    
    {'user1':'Pam Beesly', 'user2':'Andy Bernard', 'weight':0.4},
    {'user1':'Pam Beesly', 'user2':'Stanley Hudson', 'weight':0.3},
    {'user1':'Pam Beesly', 'user2':'Phillis Lapin-Vance', 'weight':0.3},
    {'user1':'Pam Beesly', 'user2':'Angela Martin', 'weight':0.3},
    {'user1':'Pam Beesly', 'user2':'Kevin Malone', 'weight':0.3},
    {'user1':'Pam Beesly', 'user2':'Oscar Martinez', 'weight':0.4},
    {'user1':'Pam Beesly', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Pam Beesly', 'user2':'Kelly Kapoor', 'weight':0.1},
    {'user1':'Pam Beesly', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Pam Beesly', 'user2':'Ryan Howard', 'weight':0.7},
    
    {'user1':'Andy Bernard', 'user2':'Stanley Hudson', 'weight':0.5},
    {'user1':'Andy Bernard', 'user2':'Phillis Lapin-Vance', 'weight':0.3},
    {'user1':'Andy Bernard', 'user2':'Angela Martin', 'weight':0.8},
    {'user1':'Andy Bernard', 'user2':'Kevin Malone', 'weight':0.3},
    {'user1':'Andy Bernard', 'user2':'Oscar Martinez', 'weight':0.2},
    {'user1':'Andy Bernard', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Andy Bernard', 'user2':'Kelly Kapoor', 'weight':0.5},
    {'user1':'Andy Bernard', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Andy Bernard', 'user2':'Ryan Howard', 'weight':0.2},
    
    {'user1':'Stanley Hudson', 'user2':'Phillis Lapin-Vance', 'weight':0.6},
    {'user1':'Stanley Hudson', 'user2':'Angela Martin', 'weight':0.3},
    {'user1':'Stanley Hudson', 'user2':'Kevin Malone', 'weight':0.5},
    {'user1':'Stanley Hudson', 'user2':'Oscar Martinez', 'weight':0.3},
    {'user1':'Stanley Hudson', 'user2':'Meredith Palmer', 'weight':0.6},
    {'user1':'Stanley Hudson', 'user2':'Kelly Kapoor', 'weight':0.3},
    {'user1':'Stanley Hudson', 'user2':'Creed Bratton', 'weight':0.5},
    {'user1':'Stanley Hudson', 'user2':'Ryan Howard', 'weight':0.2},
    
    {'user1':'Phillis Lapin-Vance', 'user2':'Angela Martin', 'weight':0.3},
    {'user1':'Phillis Lapin-Vance', 'user2':'Kevin Malone', 'weight':0.5},
    {'user1':'Phillis Lapin-Vance', 'user2':'Oscar Martinez', 'weight':0.5},
    {'user1':'Phillis Lapin-Vance', 'user2':'Meredith Palmer', 'weight':0.3},
    {'user1':'Phillis Lapin-Vance', 'user2':'Kelly Kapoor', 'weight':0.5},
    {'user1':'Phillis Lapin-Vance', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Phillis Lapin-Vance', 'user2':'Ryan Howard', 'weight':0.1},
    
    {'user1':'Angela Martin', 'user2':'Kevin Malone', 'weight':0.3},
    {'user1':'Angela Martin', 'user2':'Oscar Martinez', 'weight':0.1},
    {'user1':'Angela Martin', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Angela Martin', 'user2':'Kelly Kapoor', 'weight':0.2},
    {'user1':'Angela Martin', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Angela Martin', 'user2':'Ryan Howard', 'weight':0.1},
    
    {'user1':'Kevin Malone', 'user2':'Oscar Martinez', 'weight':0.4},
    {'user1':'Kevin Malone', 'user2':'Meredith Palmer', 'weight':0.6},
    {'user1':'Kevin Malone', 'user2':'Kelly Kapoor', 'weight':0.3},
    {'user1':'Kevin Malone', 'user2':'Creed Bratton', 'weight':0.5},
    {'user1':'Kevin Malone', 'user2':'Ryan Howard', 'weight':0.3},
    
    {'user1':'Oscar Martinez', 'user2':'Meredith Palmer', 'weight':0.2},
    {'user1':'Oscar Martinez', 'user2':'Kelly Kapoor', 'weight':0.2},
    {'user1':'Oscar Martinez', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Oscar Martinez', 'user2':'Ryan Howard', 'weight':0.2},
    
    {'user1':'Meredith Palmer', 'user2':'Kelly Kapoor', 'weight':0.4},
    {'user1':'Meredith Palmer', 'user2':'Creed Bratton', 'weight':0.5},
    {'user1':'Meredith Palmer', 'user2':'Ryan Howard', 'weight':0.2},
    
    {'user1':'Kelly Kapoor', 'user2':'Creed Bratton', 'weight':0.3},
    {'user1':'Kelly Kapoor', 'user2':'Ryan Howard', 'weight':0.8},
    
    {'user1':'Creed Bratton', 'user2':'Ryan Howard', 'weight':0.4},
]

connections = [
    {'name':'Familiarity', 'display_type':'force', 'data':familiarity_connections},
    {'name':'Heirarchy', 'display_type':'tree', 'data':[]}
]