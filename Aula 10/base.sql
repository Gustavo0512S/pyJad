IF OBJECT_ID('vwFatoVendas', 'V') is not null
    drop view vwFatoVendas 

exec('
    create view vwFatoVendas as
    select
        pedidos.idPedido, 
        pedidos.dataPedido,
        clientes.nomeCliente,
        vendedores.nomeVendedor,
        regionais.nomeRegional,
        produtos.nomePrduto,
        LinhasProdutos.nomeLinhaPoduto,
        itensPedido.PrecoUnitario,
        itensPedido.desconto,
        (itensPEdido.quantidade * (
            itenspedido.precoUnitario - itenspedido.desconto)
            ) as valor_total
        
        from pedidos 
        join clientes on pedidos.fkCliente = clientes.idPedido
        join vendedores on pedidos.fkVendedor = vendedores.idVendedor
        join regionais on vendedores.fkRegional = regionais.idReional
        join itensPEdido on itensPedido.fkPedido = pedidos.idPedido
        join produtos on itensPedido.fkProduto = produtos.idProduto
        join LinhasProdutos on produtos.fkLinha = LinhasProdutos.idLinhaProduto

')