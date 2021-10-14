# Generated by Django 3.0.8 on 2021-10-12 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=125)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
                'db_table': 'inv_bodega',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Categoria_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Categoria Producto',
                'verbose_name_plural': 'Categorias Productos',
                'db_table': 'inv_categoria_producto',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='CategoriaBodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=125)),
                ('descripcion_catbog', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Categoria_bodega',
                'verbose_name_plural': 'Categorias_bodegas',
                'db_table': 'inv_categoria_bodega',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=256)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Devolucion',
                'verbose_name_plural': 'Devoluciones',
                'db_table': 'inv_devolucion',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Egreso_cabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_documento', models.CharField(max_length=15)),
                ('fecha_documento', models.DateTimeField()),
                ('usuario_entrega', models.CharField(max_length=15)),
                ('usuario_recibe', models.CharField(max_length=15)),
                ('total_egreso', models.DecimalField(decimal_places=4, max_digits=16)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Egreso Cabecera',
                'verbose_name_plural': 'Egresos Cabeceras',
                'db_table': 'inv_cabecera_egreso',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='ingreso_cabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_documento', models.CharField(max_length=15)),
                ('fecha_documento', models.DateTimeField()),
                ('usuario_recibe', models.CharField(max_length=15)),
                ('usuario_entrega', models.CharField(max_length=15)),
                ('total_ingreso', models.DecimalField(decimal_places=4, max_digits=16)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Ingreso Cabecera ',
                'verbose_name_plural': 'Ingresos Cabeceras',
                'db_table': 'inv_ingreso_cabecera',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'inv_marca',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=3)),
                ('direccion', models.CharField(max_length=250)),
                ('celular', models.CharField(max_length=10)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Proovedor',
                'verbose_name_plural': 'Proovedores',
                'db_table': 'inv_proveedor',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='rol_persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Rol Persona',
                'verbose_name_plural': 'Roles De Personas',
                'db_table': 'inv_rol_persona',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.Categoria_producto')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'inv_producto',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=3)),
                ('direccion', models.CharField(max_length=250)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.IntegerField(default=1)),
                ('Rol_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.rol_persona')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'inv_persona',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='ingreso_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_ingreso', models.IntegerField()),
                ('precio_ingreso', models.DecimalField(decimal_places=4, max_digits=16)),
                ('sub_total', models.DecimalField(decimal_places=4, max_digits=16)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
                ('Ingreso_cabecera', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.ingreso_cabecera')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.producto')),
            ],
            options={
                'verbose_name': 'Ingreso Detalle',
                'verbose_name_plural': 'Ingresos Detalles',
                'db_table': 'inv_ingreso_detale',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Egreso_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_egreso', models.IntegerField()),
                ('precio_egreso', models.DecimalField(decimal_places=4, max_digits=16)),
                ('sub_total', models.DecimalField(decimal_places=4, max_digits=16)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.producto')),
                ('egreso_cabecera', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.Egreso_cabecera')),
            ],
            options={
                'verbose_name': 'Egreso Detalle',
                'verbose_name_plural': 'Egresos Detalles',
                'db_table': 'inv_egreso_detalle',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Bodega_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_existencia', models.IntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=4, max_digits=16)),
                ('precio_venta', models.DecimalField(decimal_places=4, max_digits=16)),
                ('stock_maximo', models.IntegerField()),
                ('stock_minimo', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_creacion', models.CharField(max_length=15)),
                ('usuario_modificacion', models.CharField(max_length=15)),
                ('estado', models.IntegerField(default=1)),
                ('Bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.bodega')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.producto')),
            ],
            options={
                'verbose_name': 'Bodega Producto',
                'verbose_name_plural': 'Bodegas Productos',
                'db_table': 'inv_bodegaproducto',
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.AddField(
            model_name='bodega',
            name='categoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control_inventario.CategoriaBodega'),
        ),
    ]
