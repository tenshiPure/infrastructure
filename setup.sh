yum install -y httpd php

echo "<?php echo date('Y-m-d');" > /var/www/html/index.php

service httpd start
