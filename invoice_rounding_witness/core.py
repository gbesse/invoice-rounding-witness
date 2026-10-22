from decimal import Decimal,InvalidOperation,ROUND_HALF_UP,ROUND_HALF_EVEN
from .common import integer,identifier,unique_ids

def decimal(value):
    if not isinstance(value,str) or len(value)>50:raise ValueError('decimal_string')
    result=Decimal(value)
    if not result.is_finite() or abs(result)>Decimal('1e12') or result.as_tuple().exponent < -8:raise ValueError('decimal_bounds')
    return result

def run(data):
    lines=data['lines'];places=integer(data.get('minor_places',2),0,4);rule=data.get('rounding','half_up');currency=identifier(data['currency'])
    if len(lines)>10000 or rule not in ('half_up','half_even'):raise ValueError('size_or_rule')
    unique_ids(lines);quantum=Decimal(1).scaleb(-places);rounding=ROUND_HALF_UP if rule=='half_up' else ROUND_HALF_EVEN;groups={};details=[]
    try:
        for line in lines:
            net=decimal(line['net']);rate=decimal(line['tax_rate']);key=identifier(line['tax_code'])
            if rate<0 or rate>1 or net.quantize(quantum)!=net:raise ValueError('rate_or_net_precision')
            if key in groups and groups[key]['rate']!=rate:raise ValueError('same_code_different_rate')
            tax=(net*rate).quantize(quantum,rounding=rounding);group=groups.setdefault(key,{'rate':rate,'net':Decimal(0),'line_tax':Decimal(0)});group['net']+=net;group['line_tax']+=tax
            details.append({'id':line['id'],'rounded_line_tax':str(tax)})
        categories=[];line_total=category_total=Decimal(0)
        for key,g in sorted(groups.items()):
            tax=(g['net']*g['rate']).quantize(quantum,rounding=rounding);delta=g['line_tax']-tax;line_total+=g['line_tax'];category_total+=tax
            categories.append({'tax_code':key,'net':str(g['net']),'tax_rate':str(g['rate']),'sum_line_tax':str(g['line_tax']),'rounded_category_tax':str(tax),'difference':str(delta)})
        return {'currency':currency,'rounding':rule,'categories':categories,'line_taxes':details,'sum_line_tax':str(line_total),'sum_category_tax':str(category_total),'difference':str(line_total-category_total),'scope':'comparison of declared rounding methods; no assertion of legally applicable tax treatment'}
    except InvalidOperation as error:raise ValueError('decimal') from error
