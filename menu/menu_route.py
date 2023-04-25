from user.views import register, login

menu_dict = {
    "name": "Project Main Menu",
    "description": "Pourya Mansouri sample project",
    "children": [
        {
            "name": "Register/Login",
            "description": "FREE to registration",
            "children": [{
                "name": "Register",
                "description": "FREE to registration",
                "function": register,

            },
                {
                    "name": "Login",
                    "description": "you need login to access",
                    "function": login,

                }, ]

        },
        {
            "name": "New test",
            "description": "Test list",
            "children": [{
                "name": "Corona Test",
                "description": "corona test",
                "children": []
            }]

        }

    ]
}
