helpdesk_tickets = env['helpdesk.ticket'].search([])

now = datetime.datetime.now()
threshold = datetime.timedelta(hours=1)
cutoff_time = now - threshold

for ticket in helpdesk_tickets:

    late_tickets = env['helpdesk.ticket'].search([('create_date', '<', cutoff_time), ('stage_id', '!=', 'Solved')])

    for late_ticket in late_tickets:
      record.write({
                'description': late_ticket
              })
      email_subject = "This is an alert that ticket with id {} is late".format(late_ticket)
      email_body = "This is to notify you that ticket {} is late.".format(late_ticket)
      late_ticket.message_post(
            body=email_body,
            subject=email_subject,
          )