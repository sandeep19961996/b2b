JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "pharmaXpert",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    # "site_header": "PharmaXpert",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "PharmaXpert",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "image/logo-2.PNG",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
     "welcome_sign": "Welcome to the PharmaXpert",

  
      "show_ui_builder": True,
    # Copyright on the footer
    "copyright": "PharmaXpert",

    # # The model admin to search from the search bar, search bar omitted if excluded
    #  "search_model": ["MitsProducts.id"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        # {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # model admin to link to (Permissions checked against model)
        #  {"model": "auth.User"},

        # external url that opens in a new window (Permissions can be added)
        {"name": "PharmaXpert_Home", "url": "http://127.0.0.1:8000/", "new_window": True},
        {"name": "Listings", "url": "http://127.0.0.1:8000/listing/", "new_window": True},
        {"name": "About", "url": "http://127.0.0.1:8000/about/", "new_window": True},
        {"name": "Category", "url": "http://127.0.0.1:8000/category/", "new_window": True},
        {"name": "Contact", "url": "http://127.0.0.1:8000/contact/", "new_window": True},

        

      
        
     
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "b"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "auth.user"}
    # ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        #AccountApp icon
        "Accountapp.Profile": "fas fa-users",
        "Accountapp.namecategory": "fas fa-user",
        "Accountapp.nameduretion": "fas  fa-business-time",
        "Accountapp.nametime": "fas  fa-clock",
        "Accountapp.postrequirement": "fas fa-plus",

        #B2bApp Icon
        "B2bapp.category":"fas  fa-users",
        "B2bapp.companyinfo":"fas fa-building",
        "B2bapp.product":"fas fa-lock",
        "B2bapp.sendpage":"fas fa-share",
        "B2bapp.subcategory":"fas fa-users",
        "B2bapp.subscriber":"fas fa-user",
         #CommonApp Icon 
         "Commonapp.websitelogo":"fas fa-user",
         #Franchise Icon
         "Franchiseapp.edmundproducts":"fas fa-swatchbook",
         "Franchiseapp.medfenseproducts":"fas fa-swatchbook",
         "Franchiseapp.mitsproducts":"fas fa-swatchbook",
         "Franchiseapp.rapidproducts":"fas fa-swatchbook",
         "Franchiseapp.ronishproducts":"fas fa-swatchbook",
         "Franchiseapp.send":"fas fa-share",
         "Franchiseapp.servoproducts":"fas fa-swatchbook",
          "Franchiseapp.shineproducts":"fas fa-swatchbook",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    
}
JAZZMIN_UI_TWEAKS = {

    # #  "theme": "simplex",
    "navbar_large_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-info",
    "navbar": "navbar-info navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    # "sidebar": "navbar-dark text-white",
    "navbar-header":"text-white",
    "sidebar_nav_large_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    # "theme": "cerulean",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
