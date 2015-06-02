# secret key
SECRET_KEY = "{{ _seafile_seahub_settings_secret_key.stdout }}"

## email settings

{% if not seafile_email_enable %}#{% endif %}
EMAIL_USE_TLS = {{ seafile_email_use_tls }}
{% if not seafile_email_enable %}#{% endif %}
EMAIL_HOST = '{{ seafile_email_host }}'
{% if not seafile_email_enable %}#{% endif %}
EMAIL_HOST_USER = '{{ seafile_email_user }}'
{% if not seafile_email_enable %}#{% endif %}
EMAIL_HOST_PASSWORD = '{{ seafile_email_password }}'
{% if not seafile_email_enable %}#{% endif %}
EMAIL_PORT = {{ seafile_email_port }}
{% if not seafile_email_enable %}#{% endif %}
DEFAULT_FROM_EMAIL = '{{ seafile_default_from_email }}'
{% if not seafile_email_enable %}#{% endif %}
SERVER_EMAIL = '{{ seafile_server_email }}'


HTTP_SERVER_ROOT = 'http://{{ seafile_ip_or_domain }}/seafhttp'

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = '{{ seafile_time_zone }}'

# Set this to seahub website's URL. This URL is contained in email notifications.
SITE_BASE = '{{ seafile_site_base }}'

# Set this to your website's name. This is contained in email notifications.
SITE_NAME = '{{ seafile_site_name }}'

# Set seahub website's title
SITE_TITLE = '{{ seafile_site_title }}'

# If you don't want to run seahub website on your site's root path, set this
# option to your preferred path.
# e.g. setting it to '/seahub/' would run seahub on http://example.com/seahub/.
SITE_ROOT = '{{ seafile_site_root }}'

# Whether to use pdf.js to view pdf files online. Default is `True`,  you can
# turn it off.
# NOTE: since version 1.4.
USE_PDFJS = {{ seafile_use_pdfjs }}

# Enalbe or disalbe registration on web. Default is `False`.
# NOTE: since version 1.4.
ENABLE_SIGNUP = {{ seafile_enable_signup }}

# Activate or deactivate user when registration complete. Default is `True`.
# If set to `False`, new users need to be activated by admin in admin panel.
# NOTE: since version 1.8
ACTIVATE_AFTER_REGISTRATION = {{ seafile_activate_after_registration }}

# Whether to send email when a system admin adding a new member. Default is
# `True`.
# NOTE: since version 1.4.
SEND_EMAIL_ON_ADDING_SYSTEM_MEMBER = {{ seafile_send_email_on_adding_system_member }}

# Whether to send email when a system admin resetting a user's password.
# Default is `True`.
# NOTE: since version 1.4.
SEND_EMAIL_ON_RESETTING_USER_PASSWD = {{ seafile_send_email_on_resetting_user_passwd }}

# Hide `Organization` tab.
# If you want your private seafile behave exactly like
# https://cloud.seafile.com/, you can set this flag.
CLOUD_MODE = {{ seafile_cloud_mode }}

# Online preview maximum file size, defaults to 30M.
FILE_PREVIEW_MAX_SIZE = {{ seafile_file_preview_max_size }}

# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = {{ seafile_session_cookie_age }}

# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = {{ seafile_session_save_every_request }}

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = {{ seafile_session_expire_at_browser_close }}

# Using server side crypto by default, otherwise, let user choose crypto method.
FORCE_SERVER_CRYPTO = {{ seafile_force_server_crypto }}

# Custom logo path
{% if not seafile_logo_path %}#{% endif %}
LOGO_PATH = '{{ seafile_logo_path }}'

# Custom css path
{% if not seafile_css_path %}#{% endif %}
BRANDING_CSS = '{{ seafile_css_path }}'

{% if seafile_backend in SEAFILE_EXTERNAL_BACKENDS %}
# External Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{ seafile_backend }}',
        'USER' : '{{ seafile_db_user }}',
        'PASSWORD' : '{{ seafile_db_pass }}',
        'NAME' : '{{ seafile_db_name.seahub }}',
        'HOST' : '{{ seafile_db_host }}',
        'OPTIONS': {
            "init_command": "SET storage_engine=INNODB",
        }
    }
}

{% endif %}
# For security consideration, please set to match the host/domain of your site,
# e.g., ALLOWED_HOSTS = ['.example.com'].
# Please refer to
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts for
# details.
{% if not seafile_allowed_hosts %}#{% endif %}
ALLOWED_HOSTS = {{ seafile_allowed_hosts }}
