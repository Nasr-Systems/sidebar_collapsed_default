app_name = "sidebar_collapsed_default"
app_title = "Sidebar Collapsed Default"
app_publisher = "Nasr Systems"
app_description = (
    "Collapses Sidebar by default. Helps use screen real-estate better on small screens"
)
app_email = "baaridun@gmail.com"
app_license = "mit"


# changes in hooks start
required_apps = ["frappe"]
app_include_js = ["collapse_sidebar.bundle.js"]
# changes in hooks end

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sidebar_collapsed_default/css/sidebar_collapsed_default.css"
# app_include_js = "/assets/sidebar_collapsed_default/js/sidebar_collapsed_default.js"

# include js, css files in header of web template
# web_include_css = "/assets/sidebar_collapsed_default/css/sidebar_collapsed_default.css"
# web_include_js = "/assets/sidebar_collapsed_default/js/sidebar_collapsed_default.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sidebar_collapsed_default/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sidebar_collapsed_default/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sidebar_collapsed_default.utils.jinja_methods",
# 	"filters": "sidebar_collapsed_default.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sidebar_collapsed_default.install.before_install"
# after_install = "sidebar_collapsed_default.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sidebar_collapsed_default.uninstall.before_uninstall"
# after_uninstall = "sidebar_collapsed_default.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sidebar_collapsed_default.utils.before_app_install"
# after_app_install = "sidebar_collapsed_default.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sidebar_collapsed_default.utils.before_app_uninstall"
# after_app_uninstall = "sidebar_collapsed_default.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sidebar_collapsed_default.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sidebar_collapsed_default.tasks.all"
# 	],
# 	"daily": [
# 		"sidebar_collapsed_default.tasks.daily"
# 	],
# 	"hourly": [
# 		"sidebar_collapsed_default.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sidebar_collapsed_default.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sidebar_collapsed_default.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sidebar_collapsed_default.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sidebar_collapsed_default.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sidebar_collapsed_default.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sidebar_collapsed_default.utils.before_request"]
# after_request = ["sidebar_collapsed_default.utils.after_request"]

# Job Events
# ----------
# before_job = ["sidebar_collapsed_default.utils.before_job"]
# after_job = ["sidebar_collapsed_default.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sidebar_collapsed_default.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
