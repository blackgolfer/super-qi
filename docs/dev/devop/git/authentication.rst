Authentication
==============

Connecting to GitHub with SSH
-----------------------------

You can connect to GitHub using the Secure Shell Protocol (SSH_), which provides a secure channel over an unsecured network.

.. _SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

.. topic:: Generating a new SSH key and adding it to the ssh-agent

    .. code:: shell

        ssh-keygen -t ed25519 -C "your_email@example.com"

.. topic:: Adding a new SSH key to your GitHub account

    To configure your account on GitHub.com to use your new (or existing) SSH key, you'll also need to add the key to your account.
    
.. _ssh-agent: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

.. _Gihub add ssh key: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
