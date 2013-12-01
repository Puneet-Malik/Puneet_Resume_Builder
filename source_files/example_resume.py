# an example resume source file.

# RESUME is a hash of subsections.  The simple
# subsections are stored as a hash of values, while the
# more complicated subsections are lists of hashes.
# Where possible we prefer hashes to nest under lists
# and lists to nest under hashes, with the exeception of
# the parent hash, RESUME, storing subsections as hashes.

# TODO: create a better way to store this information.
# When there's time, use lex to create a simple DSL
# that works like .md or the ascii output.
#

RESUME = {
    'CONTACT_INFO' : {
        'name' : 'Puneet Malik', 
        'address_1' : 'Bellandur', 
        'city' : 'Bangalore',
        'state' : 'KA',
        'zip' : '560030',
        'phone' : '(080) 212-1234',
        'email' : 'puneet.malik126@email.com',
    },

    'TECHNICAL_SKILLS' : [
        {
            'category': 'Languages',
            'entry': 'Python, Web Technologies'
        },
        {
              'category' : 'Frameworks',
            'entry': 'Django'
        },
        {
            'category' : 'Databases',
            'entry' : 'MySql'
        },
        {
            'category' : 'Software',
            'entry' : 'Micro Soft',
        },
        {
            'category': 'Operating Systems',
            'entry': 'Windows/Linux',
        },
        ],

    'WORK_EXPERIENCE' : [
        {
            'name' : 'Accenture',
            'location' : 'Bangalore, KA',
            'positions' : [
                {
                    'name' : 'Software Developer',
                    'dates' : 'May 2011 - Dec 2013',
                },
                ],
            'duties' : [
                """ As a software Developer need development requirements which comes to my name and fix bugs""",
                """Has to maintain a team of 3 developers""",
            ],
            },
        {
            'name' : 'HCL',
            'location' : 'Noida',
            'positions' : [
                {
                    'name' : 'OnJob Trainee', 
                    'dates' : 'May 2010 - May 2011',
                },
                ],
            'duties' : [
                """ Test roles""",
                """test 2 roles""",
            ],
        },
    ],

    'EDUCATION' : [
        {
            'name' : "BE Computer science",
            'location': "Haryana",
            'degree' : "BE, Computer Science", 
            'dates' : "Graduated 2010",
        },
        {
            'name': "Test School",
            'location': "Haryana",
            'degree': "test",
            'dates': "test",
        }
    ]
}
