Welcome to fake-email documentation!
========

.. important::

    If you have code using Telethon before its 1.0 version, you must
    read `Compatibility and Convenience`_ to learn how to migrate.

What is this?
-------------

It is a temporary email app to receive all messages, it automatically deletes the email 10 minutes after it is created

Installing
----------

.. code-block:: sh

  pip install fake-email 


Example
-----------

.. code-block:: python
    
    from fake_email import Email 

    mail=Email().Mail()
    print(mail)

    
response
-----------
 {'mail': 'mcb06928@cdfaq.com', 'session': 'lmtl7ui7lu7halsn1l7wdvba5g'}	

fetch messages
-----------

.. code-block:: python

    
    from fake_email import Email

    while True:

      mass=Email(session).inbox()
      if mass:
        print(mass)
	break
response
-----------
 {     
  'topic': 'Hi', 
  'name': 'روكس \\ RUKS', 
  'from': '**@gmail.com', 
  'to': 'knz83195@xcoxc.com', 
  'message': "Hi bro ,I'm muntazir",  
  'datetime': ['datetime']
 }

Example
-----------

.. code-block:: python
    
    from fake_email import Email 

    mail=Email().Mail()
    print(mail)

    while True:
      mass=Email(mail["session"]).inbox()
      if mass:
	print(mass)
	break
	
	
Next steps
----------

Do you like how fake-email looks? Check out `Read The Docs`_ for a more
in-depth explanation, with examples, troubleshooting issues, and more
useful information.

.. _asyncio: https://t.me/DIBIBl
.. _MTProto: https://core.telegram.org/mtproto
.. _Telegram: https://t.me/DIBIBl
.. _Compatibility and Convenience: https://docs.telethon.dev/en/stable/misc/compatibility-and-convenience.html
.. _Read The Docs: https://docs.telethon.dev

.. |logo| image:: logo.svg
    :width: 24pt
    :height: 24pt

