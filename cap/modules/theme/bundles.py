from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

css = NpmBundle(
    'scss/cap.scss',
    filters='node-scss, cleancss',
    output='gen/cap.%(version)s.css',
    npm={
        "almond": "~0.3.1",
        "bootstrap-sass": "~3.3.5",
        "font-awesome": "~4.4.0",
    }
)

js = NpmBundle(
    Bundle(
        'node_modules/almond/almond.js',
        'js/cap-build.js',
        'js/settings.js',
        'js/cap-settings.js',
        filters='uglifyjs',
    ),
    Bundle(
        # 'js/main.js',
        filters='requirejs',
    ),
    filters='jsmin',
    output="gen/cap.%(version)s.js",
    npm={
        "almond": "~0.3.1",
        "angular": "~1.4.10",
        "bootstrap": "~3.3.5",
    }
)

search_js = NpmBundle(
    'js/search.js',
    filters='requirejs',
    npm={
        "almond": "~0.3.1",
        "angular": "~1.4.9",
        "bootstrap": "~3.3.5",
    },
    output="gen/cap_search.%(version)s.js"
)

front_css = NpmBundle(
    'scss/frontpage.scss',
    filters='node-scss, cleancss',
    output='gen/cap.front.%(version)s.css',
    npm={
        "almond": "~0.3.1",
        "bootstrap-sass": "~3.3.5",
        "font-awesome": "~4.4.0",
    }
)


front_js = NpmBundle(
    'js/front/main.js',
    filters='requirejs',
    output="gen/cap.front.%(version)s.js",
    npm={
        "almond": "~0.3.1",
        "angular": "~1.4.10",
    }
)

records = NpmBundle(
    'js/records/main.js',
    filters='requirejs',
    output="gen/cap.records.%(version)s.js",
    npm={
        "almond": "~0.3.1",
        "angular": "~1.4.10",
        "angular-filter": "~0.5.1",
    }
)
