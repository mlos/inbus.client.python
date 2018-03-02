=====
Usage
=====

---------
Publisher
---------

The following sample code publishes messages to Inbus

.. code-block:: console

    import sys

    from inbus.client.publisher import Publisher

    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] + " <message> <app-name> [<app-type>]"
        sys.exit(1)


    appType = 0
    if len(sys.argv) == 4:
        appType = int(sys.argv[3])

    appName = sys.argv[2]
    message = sys.argv[1]

    p = Publisher(appName)

    p.publish(message, appType)


----------
Subscriber
----------

The following sample code subscribes to messages published to Inbus 

.. code-block:: console

    import sys
    from inbus.client.subscriber import Subscriber
    isRunning = True

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <app-name>"
        sys.exit(1)


    with Subscriber(sys.argv[1]) as s:
        while isRunning:
            try:
                payload, applicationType = s.get_published_message()
                print "Received :'" + payload + "' (Type: " + str(applicationType) + ")"
            except RuntimeError:
                print "Error receiving Inbus message"
            except KeyboardInterrupt:
                print "Exiting..."
                isRunning = False
