.. _apis:

APIs Design
===========

Assuming that base resource is ``/api/v1/accounts/``

Register
--------

.. data:: POST: /register/

    Register new user

.. data:: GET: /activate/<uidbase64>/<token>

    Activate account by token sent to email

Login
-----

.. data:: POST: /login/

    Login to the system use username/email and password

Social Login
-----

.. data:: POST: /login/social/

    Login to the system use ``provider`` and ``access_token``

Logout
------

.. data:: POST: /logout/

    Logout of the system

Profile
-------

.. data:: GET: /profile/

    Get user profile

.. data:: PUT: /profile/

    Update user profile

Change password
---------------

.. data:: PUT: /change-password/

    Change user password

Reset password
--------------

.. data:: POST: /reset-password/

    Reset user password by email

Set password
--------------

.. data:: PUT: /set-password/

    Set use password when login by socials
