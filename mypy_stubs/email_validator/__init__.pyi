from typing import Any, Optional

ATEXT: str
DOT_ATOM_TEXT: Any
ATEXT_UTF8: Any
DOT_ATOM_TEXT_UTF8: Any
ATEXT_HOSTNAME: str
EMAIL_MAX_LENGTH: int
LOCAL_PART_MAX_LENGTH: int
DOMAIN_MAX_LENGTH: int
unicode_class = str
DEFAULT_TIMEOUT: int

class EmailNotValidError(ValueError): ...
class EmailSyntaxError(EmailNotValidError): ...
class EmailUndeliverableError(EmailNotValidError): ...

class ValidatedEmail:
    original_email: Any = ...
    email: Any = ...
    local_part: Any = ...
    domain: Any = ...
    ascii_email: Any = ...
    ascii_local_part: Any = ...
    ascii_domain: Any = ...
    smtputf8: Any = ...
    mx: Any = ...
    mx_fallback_type: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __self__(self) -> Any: ...
    def __getitem__(self, key: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def as_constructor(self) -> str: ...
    def as_dict(self) -> dict: ...

def caching_resolver(timeout: Any = ..., cache: Optional[Any] = ...) -> Any: ...
def validate_email(
    email: Any,
    allow_smtputf8: bool = ...,
    allow_empty_local: bool = ...,
    check_deliverability: bool = ...,
    timeout: Any = ...,
    dns_resolver: Optional[Any] = ...,
) -> Any: ...
def validate_email_local_part(local: Any, allow_smtputf8: bool = ..., allow_empty_local: bool = ...) -> Any: ...
def validate_email_domain_part(domain: Any) -> Any: ...
def validate_email_deliverability(
    domain: Any, domain_i18n: Any, timeout: Any = ..., dns_resolver: Optional[Any] = ...
) -> Any: ...
def main() -> None: ...
