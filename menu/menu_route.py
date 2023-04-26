from user.views import register, login, logout

menu_dict = {
    "name": "Project Main Menu",
    "description": "Pourya Mansouri sample project",
    "children": [
        # {
        #     "name": "Register/Login",
        #     "description": "FREE to registration",
        #     "children": [{
        #         "name": "Register",
        #         "description": "FREE to registration",
        #         "function": register,

        #     },
        #         {
        #             "name": "Login",
        #             "description": "you need login to access",
        #             "function": login,

        #         }, ]

        # },
        {
            "name": "Profile",
            "description": "User account",
            "children":
                [
                    {
                        "name": "Inbox",
                        "description": "User's received messages",
                        "function": lambda: show_table_content('inbox')
                    },
                    {
                        "name": "Draft",
                        "description": "User's draft messages",
                        "function": lambda: show_table_content('draft')
                    },
                    {
                        "name": "Sent",
                        "description": "User's sent messages",
                        "function": lambda: show_table_content('sent')
                    }
                ]            
        },
        {
            "name": "Register",
            "description": "Create a new account",
            "function": register
        },
        {
            "name": "Login",
            "description": "Login to your account",
            "function": login
        },
        {
            "name": "Logout",
            "description": "Logout from your account",
            "function": logout
        }
    ]
}
