class TicketInfo:
    kind = ''
    num = ''
    price = ''


class SingleTicket:
    id_ = ''
    name = ''
    catalog = ''
    from_ = ''
    from_date = ''
    from_time = ''
    to = ''
    to_date = ''
    to_time = ''
    tickets = []

    def ticket_info(self):
        return ' / '.join(map(lambda info: '{} {}元 余{}张'.format(info.kind, info.price, info.num), self.tickets))
