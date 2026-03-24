from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random
from apps.accounts.models import Department, Role, UserProfile
from apps.customer.models import Customer, Quotation
from apps.service_order.models import WorkOrder, Feedback
from apps.product.models import Category as ProductCategory, Product, BOM
from apps.warehouse.models import PurchaseOrder, Inventory, InventoryTransaction
from apps.mall.models import MallOrder
from apps.ai_chatbot.models import ChatSession, ChatMessage
from apps.message_center.models import Message
from apps.knowledge_base.models import KnowledgeCategory, KnowledgeArticle
from apps.system_management.models import SystemConfig


class Command(BaseCommand):
    help = '生成测试数据'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help='要创建的用户数量')
        parser.add_argument('--departments', type=int, default=5, help='要创建的部门数量')
        parser.add_argument('--roles', type=int, default=5, help='要创建的角色数量')
        parser.add_argument('--customers', type=int, default=20, help='要创建的客户数量')
        parser.add_argument('--quotations', type=int, default=30, help='要创建的报价单数量')
        parser.add_argument('--work_orders', type=int, default=50, help='要创建的工单数量')
        parser.add_argument('--products', type=int, default=15, help='要创建的产品数量')
        parser.add_argument('--inventories', type=int, default=15, help='要创建的库存记录数量')
        parser.add_argument('--mall_orders', type=int, default=25, help='要创建的商城订单数量')

    def handle(self, *args, **options):
        fake = Faker('zh_CN')  # 使用中文假数据
        num_users = options['users']
        num_departments = options['departments']
        num_roles = options['roles']
        num_customers = options['customers']
        num_quotations = options['quotations']
        num_work_orders = options['work_orders']
        num_products = options['products']
        num_inventories = options['inventories']
        num_mall_orders = options['mall_orders']

        self.stdout.write("开始生成测试数据...")

        # --- 1. 生成系统配置 ---
        self.stdout.write("生成系统配置...")
        SystemConfig.objects.get_or_create(
            key='company_name',
            defaults={'value': '快工单科技有限公司', 'description': '公司名称'}
        )
        SystemConfig.objects.get_or_create(
            key='default_language',
            defaults={'value': 'zh-hans', 'description': '默认语言'}
        )

        # --- 2. 生成基础数据：部门、角色、产品分类 ---
        self.stdout.write(f"生成 {num_departments} 个部门...")
        departments = []
        for i in range(num_departments):
            dept, created = Department.objects.get_or_create(name=fake.company())
            departments.append(dept)

        self.stdout.write(f"生成 {num_roles} 个角色...")
        roles = []
        for i in range(num_roles):
            role_name = random.choice(['销售', '技术', '客服', '经理', '财务', '运维', '市场'])
            role, created = Role.objects.get_or_create(
                name=role_name,
                defaults={'permissions': ['view_all']}  # 可以扩展权限
            )
            roles.append(role)

        self.stdout.write("生成产品分类...")
        product_categories = []
        for i in range(3):
            cat_name = random.choice(['软件', '硬件', '服务', '配件'])
            cat, created = ProductCategory.objects.get_or_create(name=cat_name)
            product_categories.append(cat)

        # --- 3. 生成用户和员工档案 ---
        self.stdout.write(f"生成 {num_users} 个用户和员工档案...")
        users = []
        for i in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = 'password123'  # 测试密码

            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.save()

            user_profile = UserProfile.objects.create(
                user=user,
                department=random.choice(departments),
                role=random.choice(roles),
            )
            users.append(user)

        # --- 4. 生成产品和BOM ---
        self.stdout.write(f"生成 {num_products} 个产品...")
        products = []
        for i in range(num_products):
            product = Product.objects.create(
                name=fake.catch_phrase(),
                code=f'PROD-{i + 1:03}',
                category=random.choice(product_categories),
                unit_price=random.uniform(10.0, 1000.0),
                cost_price=random.uniform(5.0, 500.0),
                description=fake.text(max_nb_chars=200),
                min_stock=random.randint(0, 10)
            )
            products.append(product)

        self.stdout.write("生成物料清单(BOM)...")
        for product in products[:len(products) // 2]:
            other_products = [p for p in products if p != product]
            if other_products:
                components = random.sample(other_products, k=min(random.randint(1, 3), len(other_products)))
                for comp in components:
                    BOM.objects.get_or_create(
                        product=product,
                        component=comp,
                        defaults={'quantity': random.randint(1, 5)}
                    )

        # --- 5. 生成客户 ---
        self.stdout.write(f"生成 {num_customers} 个客户...")
        customers = []
        for i in range(num_customers):
            customer = Customer.objects.create(
                name=fake.company(),
                type=random.choice(['individual', 'enterprise']),
                contact_person=fake.name(),
                phone=fake.phone_number(),
                email=fake.email(),
                address=fake.address(),
                level=random.choice(['VIP', '普通', '重要']),
                credit_score=random.randint(0, 100)
            )
            customers.append(customer)

        # --- 6. 生成关联数据 ---

        # 报价单
        self.stdout.write(f"生成 {num_quotations} 个报价单...")
        for _ in range(num_quotations):
            Quotation.objects.create(
                customer=random.choice(customers),
                title=fake.sentence(nb_words=4),
                content=fake.paragraph(),
                total_amount=random.uniform(100.0, 10000.0),
                status=random.choice(['draft', 'sent', 'confirmed', 'rejected'])
            )

        # 工单
        self.stdout.write(f"生成 {num_work_orders} 个工单...")
        for _ in range(num_work_orders):
            work_order = WorkOrder.objects.create(
                customer=random.choice(customers),
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(),
                priority=random.choice([1, 2, 3]),
                status=random.choice(['pending', 'assigned', 'in_progress', 'completed', 'closed']),
                assigned_to=random.choice([up for up in UserProfile.objects.all()])
            )

            # 为部分工单生成反馈
            if random.choice([True, False, False]):  # 增加概率为False，使反馈更稀少
                Feedback.objects.create(
                    work_order=work_order,
                    satisfaction_rating=random.randint(1, 5),
                    comments=fake.sentence(nb_words=10)
                )

        # 采购订单
        self.stdout.write("生成采购订单...")
        for i in range(10):
            PurchaseOrder.objects.create(
                po_number=f'PO-{i + 1:03}',
                supplier=fake.company(),
                total_amount=random.uniform(500.0, 5000.0),
                status=random.choice(['draft', 'submitted', 'approved', 'received', 'cancelled'])
            )

        # 库存 (Inventory 不直接创建，通过事务触发)
        self.stdout.write(f"生成 {num_inventories} 个库存记录...")
        for product in random.sample(products, num_inventories):
            # 直接创建库存记录
            Inventory.objects.update_or_create(
                product=product,
                defaults={
                    'quantity_on_hand': random.randint(0, 100),
                    'quantity_reserved': random.randint(0, 20),
                }
            )

        # 库存交易
        self.stdout.write("生成库存交易记录...")
        for _ in range(20):
            InventoryTransaction.objects.create(
                product=random.choice(products),
                transaction_type=random.choice(['in', 'out']),
                quantity=random.randint(1, 20),
                reference_doc=fake.uuid4(),
                notes=fake.sentence(nb_words=5)
            )

        # 商城订单
        self.stdout.write(f"生成 {num_mall_orders} 个商城订单...")
        for _ in range(num_mall_orders):
            # 构造随机的订单项
            order_items = []
            for _ in range(random.randint(1, 3)):
                item_product = random.choice(products)
                order_items.append({
                    "product_id": item_product.id,
                    "quantity": random.randint(1, 5),
                    "price": float(item_product.unit_price)
                })

            MallOrder.objects.create(
                customer=random.choice(customers),
                order_number=fake.uuid4(),
                items=order_items,
                total_amount=random.uniform(50.0, 500.0),
                status=random.choice(['pending_payment', 'paid', 'shipped', 'delivered', 'cancelled']),
                shipping_address=fake.address()
            )

        # 知识库
        self.stdout.write("生成知识库分类和文章...")
        kb_categories = []
        for i in range(3):
            cat_name = random.choice(['常见问题', '操作指南', '更新日志', 'API文档'])
            cat, created = KnowledgeCategory.objects.get_or_create(name=cat_name, defaults={'description': fake.text()})
            kb_categories.append(cat)

        for i in range(10):
            KnowledgeArticle.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=5),
                author=fake.name(),
                category=random.choice(kb_categories),
                tags=f','.join([fake.word() for _ in range(3)]),
                is_published=True
            )

        # AI聊天
        self.stdout.write("生成AI聊天记录...")
        for customer in random.sample(customers, 5):
            session = ChatSession.objects.create(
                customer=customer,
                session_id=fake.uuid4(),
            )
            for _ in range(random.randint(2, 6)):
                ChatMessage.objects.create(
                    session=session,
                    role=random.choice(['user', 'assistant']),
                    content=fake.sentence(nb_words=8),
                )

        # 消息中心
        self.stdout.write("生成消息中心数据...")
        all_user_profiles = list(UserProfile.objects.all())
        for user_profile in random.sample(all_user_profiles, min(5, len(all_user_profiles))):
            Message.objects.create(
                recipient_user=user_profile,
                title=fake.sentence(nb_words=4),
                content=fake.paragraph(nb_sentences=2),
                message_type=random.choice(['notification', 'alert', 'reminder'])
            )

        self.stdout.write(
            self.style.SUCCESS(f'成功生成全部测试数据！')
        )
        self.stdout.write(f'- 用户: {len(users)}, 部门: {len(departments)}, 角色: {len(roles)}')
        self.stdout.write(f'- 客户: {len(customers)}, 产品: {len(products)}, 工单: {num_work_orders}')
        self.stdout.write(f'- 报价单: {num_quotations}, 商城订单: {num_mall_orders}')

