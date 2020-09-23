.. _profile:

Profile
=======

.. data:: PROFILE_SERIALIZER

    Profile serializer dotted path

    Default: ``'drf_registration.api.profile.ProfileSerializer'``

.. data:: LOGIN_PERMISSION_CLASSES

    Profile permission classes dotted paths

    Default:

    .. code:: python

        [
            'rest_framework.permissions.IsAuthenticated',
        ],
