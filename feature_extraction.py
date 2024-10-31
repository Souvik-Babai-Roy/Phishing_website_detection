import re
import pandas as pd
from urllib.parse import urlparse


def calculate_entropy(s):
    # Basic entropy calculation placeholder
    import math
    prob = [float(s.count(c)) / len(s) for c in dict.fromkeys(list(s))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy


def extract_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    # URL-based features
    features = {
        'url_length': len(url),
        'number_of_dots_in_url': url.count('.'),
        'having_repeated_digits_in_url': int(any(url[i] == url[i + 1] for i in range(len(url) - 1))),
        'number_of_digits_in_url': sum(c.isdigit() for c in url),
        'number_of_special_char_in_url': len(re.findall(r'[@$%&!*]', url)),
        'number_of_hyphens_in_url': url.count('-'),
        'number_of_underline_in_url': url.count('_'),
        'number_of_slash_in_url': url.count('/'),
        'number_of_questionmark_in_url': url.count('?'),
        'number_of_equal_in_url': url.count('='),
        'number_of_at_in_url': url.count('@'),
        'number_of_dollar_in_url': url.count('$'),
        'number_of_exclamation_in_url': url.count('!'),
        'number_of_hashtag_in_url': url.count('#'),
        'number_of_percent_in_url': url.count('%'),
        'domain_length': len(domain),
        'number_of_dots_in_domain': domain.count('.'),
        'number_of_hyphens_in_domain': domain.count('-'),
        'having_special_characters_in_domain': int(any(c in '@$%!*' for c in domain)),
        'number_of_special_characters_in_domain': sum(c in '@$%!*' for c in domain),
        'having_digits_in_domain': int(any(c.isdigit() for c in domain)),
        'number_of_digits_in_domain': sum(c.isdigit() for c in domain),
        'having_repeated_digits_in_domain': int(any(domain[i] == domain[i + 1] for i in range(len(domain) - 1))),
        'number_of_subdomains': len(domain.split('.')) - 2,
        'having_dot_in_subdomain': int(any(sub == '.' for sub in domain.split('.'))),
        'having_hyphen_in_subdomain': int(any('-' in sub for sub in domain.split('.'))),
        'average_subdomain_length': sum(len(sub) for sub in domain.split('.')) / len(domain.split('.')),
        'average_number_of_dots_in_subdomain': sum(sub.count('.') for sub in domain.split('.')) / len(
            domain.split('.')),
        'average_number_of_hyphens_in_subdomain': sum(sub.count('-') for sub in domain.split('.')) / len(
            domain.split('.')),
        'having_special_characters_in_subdomain': int(any(c in '@$%!*' for sub in domain.split('.') for c in sub)),
        'number_of_special_characters_in_subdomain': sum(c in '@$%!*' for sub in domain.split('.') for c in sub),
        'having_digits_in_subdomain': int(any(c.isdigit() for sub in domain.split('.') for c in sub)),
        'number_of_digits_in_subdomain': sum(c.isdigit() for sub in domain.split('.') for c in sub),
        'having_repeated_digits_in_subdomain': int(
            any(sub[i] == sub[i + 1] for sub in domain.split('.') for i in range(len(sub) - 1))),

        # Path-based features
        'having_path': int(bool(path)),
        'path_length': len(path),

        # Query and Fragment features
        'having_query': int(bool(parsed_url.query)),
        'having_fragment': int(bool(parsed_url.fragment)),
        'having_anchor': int(bool(parsed_url.fragment)),

        # Entropy-based features
        'entropy_of_url': calculate_entropy(url),
        'entropy_of_domain': calculate_entropy(domain)
    }

    return pd.DataFrame([features])
