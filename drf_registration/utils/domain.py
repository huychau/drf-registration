from drf_registration.settings import drfr_settings


def get_current_domain(request):
    """
    Get current domain

    Args:
        request (object): The request object from user
    Returns:
        [str]: Current domain name
    """

    return drfr_settings.PROJECT_BASE_URL or f'{request.scheme}://{request.get_host()}'
